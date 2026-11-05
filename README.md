# tademarozsak.github.io

Personal academic website. Plain Jekyll, built automatically by GitHub Pages on every push to `main`. No theme, no Sass, and JavaScript only where a page needs it (maths rendering and the research toggle's shareable links).

## Where things live

| To change…                         | Edit                                   |
| ---------------------------------- | -------------------------------------- |
| Name, tagline, site description    | `_config.yml`                          |
| Bio and photo on the home page     | `index.html`, `assets/img/profile.jpg` |
| Home page links (order, add, hide) | `_data/links.yml`                      |
| Research projects (cards)          | `_projects/<name>.md`: name, one sentence, image, order |
| Research texts (two versions)      | `_includes/research/<name>/introductory.md`, `technical.md` |
| Publications                       | `_data/publications.yml`               |
| CV                                 | replace `cv/CV.pdf`                    |
| `<head>` (fonts, meta, CSS)        | `_includes/head.html`                  |
| Inner page frame (sticky bar, title) | `_layouts/page.html` |
| Icons                              | `_includes/icons/*.svg`                |
| Styles                             | `_includes/css/*.css` (see below)      |

```
_config.yml          site settings
_layouts/            base.html (every page) → page.html (inner pages) → project.html (research projects)
_includes/           head, project card, publication entry, research texts, icons/, css/
_data/               links.yml, publications.yml
_projects/           one file per research project
_tools/              scripts that make the project card images (not published)
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
fill: true                # instead, for full-width content that reaches the bottom of the window (like the CV)
---
```

Every page except the home page uses `layout: page`. That layout draws the bar (Home + the site's pages) and the title, so they look and sit the same on every page. Don't write them inside a page.

Then add it to `_data/links.yml` if it should appear on the home page.

## Writing content

- **Citations:** Markdown footnotes. Write `[^name]` after the sentence and `[^name]: Author, A. et al. Title. *Journal* **vol**, pages (year). [doi:…](https://doi.org/…)` at the bottom. They number themselves. For two citations side by side, write `[^a]<sup>,</sup>[^b]` so they read "4,5". On the research page, names in `technical.md` start with `t-` so they don't clash with the introductory version.
- **Maths:** add `math: true` to the page's front matter (loads KaTeX). Inline: `$$3\omega$$` inside a sentence. Display: `$$ … $$` as its own paragraph. Plain `\( \)` doesn't work in Markdown because the backslash is eaten.
- **Research projects:** each project is a file in `_projects/` (card `name`, one-sentence `description`, `image`, `order`, and `heading`: the one title both versions share) plus a folder `_includes/research/<same name>/` with `introductory.md` and `technical.md`. The texts have no title of their own; a `##` heading in them shows a red warning on the page. It gets its own page at `/research/<name>/` and a card above the toggle on every project page. The first project uses `permalink: /research/`. Card images: square, at least 200×200 px, in `assets/img/projects/`.
- **Research toggle:** `#technical` on any project page (e.g. `/research/#technical`) opens the technical view directly, which is handy for sharing with colleagues. Otherwise each visitor's last choice is remembered in their browser, so it stays the same when they switch projects.

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
   - `.segmented`: a pill of mutually exclusive options (radio buttons), e.g. the research toggle.
   - `.page-bar` (sticky bar) and `.page-title` (large title): only ever drawn by the `page` layout. The home page has no bar. The bar's menu, on the right, is Home plus the internal links (`/…`) in `_data/links.yml`, minus the page you're on; uncommenting Publications there adds it to the bar too. The large title sits in the bar's left slot, its top level with the menu, and shrinks in place as you scroll (phones too). On wide screens the research toggle docks in the middle of the bar; on phones, where the bar is slimmer, it docks in a full-width strip under it. Switching version while reading further down jumps to the start of the other text.
   Don't make one-off variants. Add a modifier, and add it to the style guide.
5. **Focus:** every focusable thing shows `--focus-ring` when reached by keyboard.
6. **Icons:** Heroicons outline, 24px viewBox, `stroke-width="2"`, one file each in `_includes/icons/`, included with `{% include icons/name.svg %}`. They inherit text colour and are sized by `.icon` (or `.icon--xl`). One meaning per icon.
7. **Fonts:** one font, DM Serif Text (400 + italic), for everything: text, headings, links, buttons and the toggle. Load only weights that are used. DM Serif Text has no bold, so headings are 400 (`--font-weight-heading`).
8. **Motion:** only via `--duration-*` / `--ease-*`. Changing page is a short cross-fade (`base.css`); nothing slides between pages. Reduced-motion users get no animation (handled globally in `base.css`).
9. **Links:** pages on this site, email and documents open in the same tab; external sites linked from the home page (the lab and the navigation links with `://`) open in a new tab. Internal URLs start with `/` and go through `relative_url` in templates.
10. **Pages:** every inner page uses `layout: page` (the home page uses `base`), so the `<head>`, sticky bar and title are never written by hand. If a page needs a different frame, add a front-matter option to `page.html` (like `prose` or `fill`) rather than a new header.
