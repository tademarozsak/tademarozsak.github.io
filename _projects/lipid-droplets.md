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
Lipid droplets are where cells store fat, and their size says something about how a cell is using those reserves. Third-harmonic generation (THG) microscopy can image them in living cells without any labels: a tightly focused laser produces light at three times its frequency wherever the optical properties of the sample change sharply, and the edge of a droplet is exactly such a place.

Reading a droplet's size off a THG image is harder than it looks. The droplet bends the focused light, the signal from different parts of it adds up or cancels, and the microscope collects only part of what comes out. How large and how bright a droplet appears therefore depends on the focus as much as on the droplet.

I'm building a model that follows the light from the laser, through the droplet, to the detector, so that a droplet's size and optical properties can be worked out from its image. The simulations are in place, and I'm now comparing them with measurements on beads of known size.
