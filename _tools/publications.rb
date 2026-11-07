# Fills _data/publications.yml (the list on /publications/) from your ORCID
# record, with the details (authors, journal, volume, article number) from
# Crossref, using each paper's DOI.
#
# Run it after a new paper appears on ORCID, from the site's folder:
#     /opt/homebrew/opt/ruby@3.3/bin/ruby _tools/publications.rb
# then check the diff of _data/publications.yml and commit.
#
# What survives a re-run (edit these by hand in _data/publications.yml):
#   equal: N       the first N authors contributed equally (marked †)
#   arxiv: 'id'    the preprint (e.g. '2512.22980'); the title links to it
#                  until there is a DOI, and a research page can name it
#   entries without a doi (e.g. an accepted paper): kept as they are until
#                  ORCID lists a paper with the same title; that one then
#                  replaces it and takes over its equal and arxiv.
#
# Ruby, because Jekyll already needs it; only the standard library is used.
# Jekyll ignores this folder (leading underscore), so it is not published.
require "date"
require "json"
require "net/http"
require "uri"
require "yaml"

SITE = File.expand_path("..", __dir__)
DATA = File.join(SITE, "_data", "publications.yml")
CONFIG = YAML.load_file(File.join(SITE, "_config.yml"))
ORCID = CONFIG.fetch("orcid")
ME = CONFIG.fetch("author")   # your name as printed on your papers
HAND_FIELDS = %w[equal arxiv].freeze

HEADER = <<~YAML
  # Publications, newest first, shown on /publications/.
  # Made by _tools/publications.rb from ORCID and Crossref: run it again after
  # a new paper appears on ORCID. Hand edits that survive a re-run:
  #   equal: N       the first N authors contributed equally (marked †)
  #   arxiv: 'id'    the preprint; the title links to it until there is a DOI
  #   an entry without a doi (e.g. an accepted paper), with title, authors,
  #   year, journal and status; it stays until ORCID lists the same title.
YAML

def get_json(url, accept: "application/json")
  uri = URI(url)
  request = Net::HTTP::Get.new(uri, "Accept" => accept,
                                    "User-Agent" => "tademarozsak.github.io publications script")
  response = Net::HTTP.start(uri.host, uri.port, use_ssl: true) { |http| http.request(request) }
  raise "#{url}: HTTP #{response.code}" unless response.is_a?(Net::HTTPSuccess)
  JSON.parse(response.body)
end

# Accents and case don't matter when matching names and titles.
def plain(text)
  text.unicode_normalize(:nfd).gsub(/\p{Mn}/, "").downcase.gsub(/[^a-z0-9]+/, " ").strip
end

def unescape(text)
  text.gsub("&amp;", "&").gsub(/<[^>]+>/, "")
end

def dois_from_orcid
  works = get_json("https://pub.orcid.org/v3.0/#{ORCID}/works")
  works.fetch("group").filter_map do |group|
    ids = group.dig("external-ids", "external-id") || []
    doi = ids.find { |id| id["external-id-type"] == "doi" }
    doi && doi["external-id-value"].downcase
  end.uniq
end

def from_crossref(doi)
  work = get_json("https://api.crossref.org/works/#{URI.encode_www_form_component(doi)}").fetch("message")
  authors = work.fetch("author").map do |a|
    name = [a["given"], a["family"]].compact.join(" ")
    plain(name) == plain(ME) ? ME : name   # your name spelled the site's way
  end
  {
    "title" => unescape(work.fetch("title").first),
    "authors" => authors,
    "year" => work.dig("issued", "date-parts", 0, 0),
    "date" => work.dig("issued", "date-parts", 0).map { |n| n.to_s.rjust(2, "0") }.join("-"),
    "journal" => unescape(work.fetch("container-title").first),
    "volume" => work["volume"],
    "number" => work["article-number"] || work["page"]&.sub("-", "–"),
    "doi" => doi,
  }.compact
end

existing = File.exist?(DATA) ? (YAML.load_file(DATA) || []) : []
by_doi = existing.select { |e| e["doi"] }.to_h { |e| [e["doi"].downcase, e] }
by_title = existing.reject { |e| e["doi"] }.to_h { |e| [plain(e["title"]), e] }

fetched = dois_from_orcid.map do |doi|
  entry = from_crossref(doi)
  before = by_doi[doi] || by_title.delete(plain(entry["title"]))
  HAND_FIELDS.each { |field| entry[field] = before[field] if before&.key?(field) }
  puts "#{before ? "updated" : "added  "}  #{entry["year"]}  #{entry["title"]}"
  entry
end

kept = by_title.values
kept.each { |entry| puts "kept     #{entry["year"]}  #{entry["title"]} (no doi yet)" }

# Newest first; an accepted paper (no date yet) goes on top of its year.
all = (fetched + kept).sort_by do |e|
  [-e["year"].to_i, e["date"] ? 1 : 0, e["date"] ? -Date.parse(e["date"]).jd : 0]
end

File.write(DATA, HEADER + "\n" + all.to_yaml(line_width: -1).sub(/\A---\n/, ""))
puts "wrote #{all.size} publications to #{DATA.sub(SITE + "/", "")}"
