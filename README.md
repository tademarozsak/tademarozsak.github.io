# tademarozsak.github.io

Personal academic website. Plain Jekyll, built automatically by GitHub Pages on every push to `main`. No theme, no Sass, and JavaScript only where a page needs it (maths rendering and the research toggle's shareable links).

## Where things live

| To change…                         | Edit                                   |
| ---------------------------------- | -------------------------------------- |
| Name, tagline, site description    | `_config.yml`                          |
| Bio and photo on the home page     | `index.html`, `assets/img/profile.jpg` |
| Home page links (order, add, hide) | `_data/links.yml`                      |
| Research text (two versions)       | `_includes/research/introductory.md`, `technical.md` |
| Publications                       | `_data/publications.yml`               |
| CV                                 | replace `cv/CV.pdf`                    |
| `<head>` (fonts, meta, CSS)        | `_includes/head.html`                  |
| Inner page frame (back link, title) | `_layouts/page.html`, `_includes/back-link.html` |
| Icons                              | `_includes/icons/*.svg`                |
| Styles                             | `_includes/css/*.css` (see below)      |

```
_config.yml          site settings
_layouts/            base.html (every page) → page.html (inner pages)
_includes/           head, back link, publication entry, icons/, css/
_data/               links.yml, publications.yml
assets/              css/main.css (joins the partials), img/
index.html  research.html  publications.html  cv/  404.html  styleguide.html
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

Every page except the home page uses `layout: page`. That layout draws the back link and title, so they look and sit the same on every page. Don't write them inside a page.

Then add it to `_data/links.yml` if it should appear on the home page.

## Writing content

- **Citations:** Markdown footnotes. Write `[^name]` after the sentence and `[^name]: Author, A. et al. Title. *Journal* **vol**, pages (year). [doi:…](https://doi.org/…)` at the bottom. They number themselves. For two citations side by side, write `[^a]<sup>,</sup>[^b]` so they read "4,5". On the research page, names in `technical.md` start with `t-` so they don't clash with the introductory version.
- **Maths:** add `math: true` to the page's front matter (loads KaTeX). Inline: `$$3\omega$$` inside a sentence. Display: `$$ … $$` as its own paragraph. Plain `\( \)` doesn't work in Markdown because the backslash is eaten.
- **Research toggle:** `/research/#technical` opens the technical view directly, which is handy for sharing with colleagues.

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
   - `.link`: UI links (navigation, actions, back link). Sans, 44px tap target, wipe on hover.
   - `.link-inline`: links inside sentences. Plain `<a>` in Markdown pages gets this automatically.
   - `.button`: the only filled control.
   - `.segmented`: a pill of mutually exclusive options (radio buttons), e.g. the research toggle.
   - `.page-header` (back link + `.page-title`): only ever drawn by the `page` layout.
   Don't make one-off variants. Add a modifier, and add it to the style guide.
5. **Focus:** every focusable thing shows `--focus-ring` when reached by keyboard.
6. **Icons:** Heroicons outline, 24px viewBox, `stroke-width="2"`, one file each in `_includes/icons/`, included with `{% include icons/name.svg %}`. They inherit text colour and are sized by `.icon` (or `.icon--xl`). One meaning per icon: arrow-left = back.
7. **Fonts:** DM Serif Text (400 + italic) for text and headings, Noto Sans 600 for UI. Load only weights that are used. DM Serif Text has no bold, so headings are 400 (`--font-weight-heading`).
8. **Motion:** only via `--duration-*` / `--ease-*`. Reduced-motion users get no animation (handled globally in `base.css`).
9. **Links:** everything opens in the same tab. Internal URLs start with `/` and go through `relative_url` in templates.
10. **Pages:** every inner page uses `layout: page` (the home page uses `base`), so the `<head>`, back link and title are never written by hand. If a page needs a different frame, add a front-matter option to `page.html` (like `prose` or `fill`) rather than a new header.
