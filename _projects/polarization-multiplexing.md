---
name: Vector beam multiplexing     # short name, on the card
heading: Multiplexed vector beam conversion via nonunitary spatial polarization transformation   # title above the summary
description: One passive device that converts up to three different polarization patterns of light, shown with optical skyrmions.
image: /assets/img/projects/polarization-multiplexing.png   # made by _tools/skyrmion_card.py
order: 2
paper: '2512.22980'        # the arXiv preprint; links to Nature Communications once the paper has a DOI
---
In a vector beam, the polarisation of light changes across the beam, so the beam carries a pattern. Optical skyrmions are patterns in which the polarisation wraps around every possible state a whole number of times. A whole number can't drift slightly, so skyrmions hold up well against distortion, which makes them interesting for carrying information.

<figure class="pol-figure">
  <div class="pol-figure__art">
    <picture>
      <source srcset="{{ '/assets/img/projects/polarization-multiplexing-animation-still.png' | relative_url }}" media="(prefers-reduced-motion: reduce)">
      <source srcset="{{ '/assets/img/projects/polarization-multiplexing-animation.webp' | relative_url }}" type="image/webp">
      <img src="{{ '/assets/img/projects/polarization-multiplexing-animation.png' | relative_url }}" width="1200" height="544" loading="lazy" decoding="async"
           alt="A Poincare sphere on the left, where a polarisation state moves around a loop through three input states; on the right, the field the device produces from it, an optical skyrmion whose pattern changes as the input moves.">
    </picture>
    <svg class="pol-figure__labels" viewBox="0 0 1200 544" aria-hidden="true">
      <defs>
      <path id="pol-figure-arc-0" data-cx="271.7" data-cy="272.0" data-r="244.5" d="M -24.2 324.2 A 300.5 300.5 0 0 0 567.6 324.2"/>
      <path id="pol-figure-arc-1" data-cx="928.3" data-cy="272.0" data-r="244.5" d="M 632.4 324.2 A 300.5 300.5 0 0 0 1224.2 324.2"/>
      </defs>
      <text text-anchor="middle"><textPath href="#pol-figure-arc-0" startOffset="50%">input polarisation</textPath></text>
      <text text-anchor="middle"><textPath href="#pol-figure-arc-1" startOffset="50%">output field</textPath></text>
    </svg>
  </div>
  <figcaption class="pol-figure__caption">
    <strong>One device, three conversions.</strong>
    As the input polarisation moves through the three designed states, the output changes between three optical skyrmions.
    Hue shows the orientation of each ellipse, lightness its handedness.
  </figcaption>
</figure>

<script>
  // Curved labels under the circles (.pol-figure__labels). The SVG scales with
  // the figure, so set its text to the caption's size (--text-sm, read from
  // .pol-figure__art) and put each arc just clear of its circle: the glyph tops
  // sit 0.3em below the circle's edge (the cap height is about 0.7em).
  (() => {
    for (const svg of document.querySelectorAll('.pol-figure__labels')) {
      const fit = () => {
        const scale = svg.getBoundingClientRect().width / svg.viewBox.baseVal.width;
        if (!scale) return;
        const size = parseFloat(getComputedStyle(svg.parentElement).fontSize) / scale;
        svg.style.fontSize = size + 'px';
        for (const path of svg.querySelectorAll('path')) {
          const { cx, cy, r } = path.dataset;
          const rr = +r + size, dx = rr * Math.sin(80 * Math.PI / 180), dy = rr * Math.cos(80 * Math.PI / 180);
          path.setAttribute('d', `M ${+cx - dx} ${+cy + dy} A ${rr} ${rr} 0 0 0 ${+cx + dx} ${+cy + dy}`);
        }
      };
      new ResizeObserver(fit).observe(svg);
    }
  })();
</script>

Devices that reshape such patterns usually perform one conversion. With colleagues at the University of Oxford, we designed a single passive device that performs three: each of three input patterns comes out as its own, unrelated output, with nothing to switch. It is a stack of three pixelated layers, two that rotate the polarisation and a partial polariser between them, which gives up some light in exchange for the freedom to map each input independently. Three conversions turn out to be the most that any passive polarisation device can perform in general.

We demonstrated it in simulation and in the lab, turning uniform beams into skyrmions of different orders and converting skyrmions from one order to another.
