# tademarozsak.github.io

Personal academic website. Plain Jekyll, built automatically by GitHub Pages on every push to `main`. No theme, no Sass, and JavaScript only where a page needs it (maths rendering, the shrinking title and docking).

## Where things live

| To change…                         | Edit                                   |
| ---------------------------------- | -------------------------------------- |
| Name, tagline, site description, ORCID and Google Scholar ids | `_config.yml` |
| Bio and photo on the home page     | `index.html`, `assets/img/portrait.jpg` (500 px, with a 10% margin around what the circle shows; see `.profile-photo` in `pages.css`) |
| Home page links (order, add, hide; `copy: true` makes Email copy the address) | `_data/links.yml` |
| Research projects                  | `_projects/<name>.md`: card, title, paper, and the summary below the front matter |
| Publications                       | run `_tools/publications.rb` (see below); hand edits in `_data/publications.yml` |
| CV                                 | replace `cv/CV.pdf` (the site draws its pages itself, see below) |
| `<head>` (fonts, meta, CSS)        | `_includes/head.html`                  |
| Inner page frame (sticky bar, title) | `_layouts/page.html` |
| Icons                              | `_includes/icons/*.svg`                |
| Styles                             | `_includes/css/*.css` (see below)      |

```
_config.yml          site settings
_layouts/            base.html (every page) → page.html (inner pages) → project.html (research projects)
_includes/           head, project card, publication entry, icons/, css/
_data/               links.yml, publications.yml
_projects/           one file per research project (card, title, paper, summary)
_tools/              scripts: project card images, the publication list (not published)
assets/              css/main.css (joins the partials), img/
index.html  publications.html  cv/  404.html  styleguide.html
```

## Adding a page

Create `something.md` (or `.html`) at the root:

```yaml
---
layout: page
title: Something          # also becomes "Something | Tade Marozsak" in the tab
description: One sentence for search results.
permalink: /something/
prose: true               # for long-form text
fill: true                # instead, for full-width content that reaches the bottom of the window, with no large title (e.g. a document viewer)
short_title: Something    # used instead of the title where the title can't fit beside the menu (e.g. CV on phones)
---
```

Every page except the home page uses `layout: page`. That layout draws the bar (Home + the site's pages) and the title, so they look and sit the same on every page. Don't write them inside a page.

Then add it to `_data/links.yml` if it should appear on the home page.

## Writing content

- **Citations:** Markdown footnotes. Write `[^name]` after the sentence and `[^name]: Author, A. et al. Title. *Journal* **vol**, pages (year). [doi:…](https://doi.org/…)` at the bottom. They number themselves. For two citations side by side, write `[^a]<sup>,</sup>[^b]` so they read "4,5".
- **Maths:** add `math: true` to the page's front matter (loads KaTeX). Inline: `$$3\omega$$` inside a sentence. Display: `$$ … $$` as its own paragraph. Plain `\( \)` doesn't work in Markdown because the backslash is eaten.
- **Research projects:** one file per project in `_projects/`, for first-author work. Front matter: the card's `name`, one-sentence `description` and `image`, its `order`, the page's title (`heading`), and `paper`: the paper's arXiv id or DOI, in quotes (`paper: '2512.22980'`). Below the front matter goes a short summary in Markdown (a few paragraphs; the paper has the details). Each project gets its own page at `/research/<name>/` and a card on every project page. The first project uses `permalink: /research/`. Card images: square, at least 200×200 px, in `assets/img/projects/`.
- **Publications:** after a new paper appears on ORCID, run `/opt/homebrew/opt/ruby@3.3/bin/ruby _tools/publications.rb`. It reads your works from ORCID and their authors, journal, volume and article number from Crossref, rewrites `_data/publications.yml` (newest first) and prints what changed. Check the diff and commit. In that file you can add `equal: N` (the first N authors contributed equally, marked †), which survives a re-run. A paper that isn't on ORCID yet (e.g. accepted) can be written in by hand without a `doi`, with `status: accepted`; it stays until ORCID lists a paper with the same title, which then replaces it. Papers are grouped by year, and the years are listed in the margin on wide screens. Titles link to the article once it has a DOI. Long author lists are shortened to the first three, you, and the last author.
- **CV:** `cv/CV.pdf` is drawn by the site with PDF.js (Mozilla's PDF library, from cdnjs, pinned to 3.11.174 with an integrity check): white pages on the site's grey, the width of the column, the same in every browser and on phones. Text can be selected and searched, the PDF's links work, and the page has the usual large title and a docked pill with zoom (− and +, from 1024px wide; 50–200%, keeping your place) and Download. Without JavaScript it offers the download.
- **Paper button:** a project's `paper` is looked up in `_data/publications.yml` (by `arxiv` or `doi`), so add the paper there first. The button docks while you read and goes to the journal once the entry has a DOI (after `_tools/publications.rb` picks it up from ORCID), or to arXiv until then. No `paper`, no button.

## Previewing locally

One-time setup: `brew install ruby@3.3`, then `bundle install`.

```bash
PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH" bundle exec jekyll serve --livereload
```

Open http://localhost:4000. After any CSS change, check **/styleguide/** (not linked from the site, not indexed). It shows every component on one page.

## Style rules

1. **Tokens only.** Every colour, size, font, radius, shadow and duration is a custom property in `_includes/css/tokens.css`. Components use the semantic names (`--color-text-muted`, `--space-5`), never hex values, raw `rem`s, or the `--gray-*` primitives. `px` only for 1px borders.
2. **CSS files and order:** `tokens` → `base` (element defaults) → `layout` (`.page`, `.stack`, `.cluster`, `.prose`) → `components` (reused anywhere) → `pages` (one section per page). If a style is used on two pages, it moves to `components`.
3. **Naming:** `block__element--modifier` (e.g. `.publication__title`, `.icon--xl`). Style with classes, not IDs or tag chains.
4. **One component per job:**
   - `.link`: UI links (navigation, actions). 44px tap target, wipe on hover.
   - `.link-inline`: links inside sentences. Plain `<a>` in Markdown pages gets this automatically. When a link in a sentence leaves the site, end it with `<span class="link-inline__arrow" aria-hidden="true">&#8617;&#xfe0e;</span>` inside the `<a>` (the same ↩︎ as the references), like the lab in the home intro.
   - `.button`: the only filled control.
   - `.segmented`: a pill of options: radio buttons, or links that fill in on hover (the paper button on Research, the profiles on Publications, zoom and Download on the CV; buttons, icon-only options and a divider are supported too).
   - `.page-toc`: the page's sections listed in the right margin (wide screens only, from 78rem), kept in view while you scroll, with the section you're reading marked; clicking one scrolls there. The `page` layout's script handles it. Used for the years on Publications.
   - `.dock`: wraps a `.segmented` that sits centred under the page's opening and docks while you read: in the middle of the bar on wide screens, in a full-width strip under the bar on phones (the bar is slimmer there). One per page; the `page` layout's script handles it, and gives a short page just enough space at the bottom to dock.
   - `.page-bar` (sticky bar) and `.page-title` (large title): only ever drawn by the `page` layout. The home page has no bar. The bar's menu, on the right, is Home plus the internal links (`/…`) in `_data/links.yml`, minus the page you're on. The large title sits in the bar's left slot, its top level with the menu, and shrinks in place as you scroll (phones too); if even the compact title doesn't fit beside the menu (a long title on a narrow phone), it stays an ordinary heading under the bar.
   Don't make one-off variants. Add a modifier, and add it to the style guide.
5. **Focus:** every focusable thing shows `--focus-ring` when reached by keyboard.
6. **Icons:** Heroicons outline, 24px viewBox, `stroke-width="2"`, one file each in `_includes/icons/`, included with `{% include icons/name.svg %}`. They inherit text colour and are sized by `.icon` (or `.icon--xl`). One meaning per icon.
7. **Fonts:** one font, DM Serif Text (400 + italic), for everything: text, headings, links and buttons. Load only weights that are used. DM Serif Text has no bold, so headings are 400 (`--font-weight-heading`).
8. **Motion:** only via `--duration-*` / `--ease-*`. Changing page is a short cross-fade (`base.css`); nothing slides between pages. The home photo comes into focus like a microscope image the first time it is shown in a visit (`--duration-focus`; script in `index.html`, keyframes in `pages.css`). Reduced-motion users get no animation (handled globally in `base.css`).
9. **Links:** pages on this site, email and documents open in the same tab; external sites linked from the home page (the lab and the navigation links with `://`) open in a new tab. Internal URLs start with `/` and go through `relative_url` in templates.
10. **Pages:** every inner page uses `layout: page` (the home page uses `base`), so the `<head>`, sticky bar and title are never written by hand. If a page needs a different frame, add a front-matter option to `page.html` (like `prose` or `fill`) rather than a new header.
