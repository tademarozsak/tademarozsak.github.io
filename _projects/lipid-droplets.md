---
# One research project: the card (name, description, image), the page's title
# (heading) and, below this front matter, a short summary in Markdown.
name: Lipid droplet imaging     # short name, on the card
heading: Third-harmonic generation for lipid droplet imaging   # title above the summary
description: Modelling how a THG microscope images lipid droplets, to measure their size in living cells without labels.
image: /assets/img/projects/lipid-droplets.png   # made by _tools/thg_card.py (square, at least 200×200 px)
order: 1                   # position of the card
permalink: /research/      # the first project is also the Research page itself
# paper: '2512.22980'      # arXiv id or DOI of the paper, once there is one (in quotes): adds a button to it
---
<figure class="thg-figure">
  <div class="thg-figure__art">
    <picture>
      <source srcset="{{ '/assets/img/projects/lipid-droplets-animation-still.png' | relative_url }}" media="(prefers-reduced-motion: reduce)">
      <source srcset="{{ '/assets/img/projects/lipid-droplets-animation.webp' | relative_url }}" type="image/webp">
      <img src="{{ '/assets/img/projects/lipid-droplets-animation.png' | relative_url }}" width="800" height="726" loading="lazy" decoding="async"
           alt="A simulated third-harmonic image of a bead on the right; on the left, the back pupil's fill, the refractive indices and the detection function, which change one at a time while the image changes with them.">
    </picture>
    <svg class="thg-figure__labels" viewBox="0 0 800 726" aria-hidden="true">
      <defs>
      <path id="thg-figure-arc-0" data-cx="208.6" data-cy="129.6" data-r="80.0" d="M 100.2 148.7 A 110.0 110.0 0 0 0 317.0 148.7"/>
      <path id="thg-figure-arc-1" data-cx="208.6" data-cy="626.3" data-r="100.1" d="M 80.5 648.9 A 130.1 130.1 0 0 0 336.7 648.9"/>
      <path id="thg-figure-arc-2" data-cx="606.1" data-cy="536.5" data-r="100.1" d="M 478.0 559.1 A 130.1 130.1 0 0 0 734.2 559.1"/>
      </defs>
    <text text-anchor="middle"><textPath href="#thg-figure-arc-0" startOffset="50%">pupil fill</textPath></text>
    <text text-anchor="middle"><textPath href="#thg-figure-arc-1" startOffset="50%">detection</textPath></text>
    <text text-anchor="middle"><textPath href="#thg-figure-arc-2" startOffset="50%">simulated THG image</textPath></text>
      <text text-anchor="middle" dominant-baseline="hanging" class="thg-figure__small" x="75.3" y="433.8">sphere</text>
      <text text-anchor="middle" dominant-baseline="hanging" class="thg-figure__small" x="199.4" y="433.8">host</text>
      <text text-anchor="middle" dominant-baseline="hanging" x="137.4" y="433.8" dy="1.1em">refractive index</text>
    </svg>
  </div>
  <figcaption class="thg-figure__caption">
    <strong>The image depends on the microscope.</strong>
    A simulated THG image of a 4 µm bead changes as the fill of the objective's back pupil, the refractive
    indices of bead and surrounding medium (light: laser, dark: third harmonic) and the detection are varied in turn.
  </figcaption>
</figure>

<script>
  // Curved labels under the pupil and the detection plot (.thg-figure__labels), as on the
  // polarisation page: the SVG scales with the figure, so set its text to the caption's size
  // (--text-sm, read from .thg-figure__art) and put each arc just clear of its circle.
  // The arcs are flatter than the circles (BEND), unlike the polarisation page's.
  (() => {
    const BEND = 1.6;
    for (const svg of document.querySelectorAll('.thg-figure__labels')) {
      const fit = () => {
        const scale = svg.getBoundingClientRect().width / svg.viewBox.baseVal.width;
        if (!scale) return;
        const size = parseFloat(getComputedStyle(svg.parentElement).fontSize) / scale;
        svg.style.fontSize = size + 'px';
        for (const path of svg.querySelectorAll('path')) {
          // baseline 1em below the circle (glyph tops 0.3em clear of it), on an arc BEND times wider than
          // the circle's own, centred higher so its lowest point stays put: flatter text
          const { cx, cy, r } = path.dataset;
          const base = +r + size, rr = BEND * base, ccy = +cy + base - rr;
          const dx = rr * Math.sin(60 * Math.PI / 180), dy = rr * Math.cos(60 * Math.PI / 180);
          path.setAttribute('d', `M ${+cx - dx} ${ccy + dy} A ${rr} ${rr} 0 0 0 ${+cx + dx} ${ccy + dy}`);
        }
      };
      new ResizeObserver(fit).observe(svg);
    }
  })();
</script>

Lipid droplets are where cells store fat, and their size says something about how a cell is using those reserves. Third-harmonic generation (THG) microscopy can image them in living cells without any labels: a tightly focused laser produces light at three times its frequency wherever the optical properties of the sample change sharply, and the edge of a droplet is exactly such a place.

Reading a droplet's size off a THG image is harder than it looks. The droplet bends the focused light, the signal from different parts of it adds up or cancels, and the microscope collects only part of what comes out. How large and how bright a droplet appears therefore depends on the focus as much as on the droplet.

I'm building a model that follows the light from the laser, through the droplet, to the detector, so that a droplet's size and optical properties can be worked out from its image. The simulations are in place, and I'm now comparing them with measurements on beads of known size.
