{%- comment -%}
  Vector beam multiplexing, introductory version (for a general audience). Markdown.
  Citations: [^name] after a sentence, [^name]: ... at the bottom; numbered automatically.
  Footnote names must not clash with technical.md (that file prefixes its names with t-).
  No title here: both versions share the project's `heading` in _projects/polarization-multiplexing.md.
{%- endcomment -%}
Light has a *polarisation*: the direction in which its electric field oscillates. In a *vector beam*, the polarisation changes from point to point, so the beam carries a pattern. In some patterns, called *optical skyrmions*, the polarisation twists through every possible state, and a whole number, the skyrmion number, counts how many times it does so.[^shen] A whole number cannot drift slightly, so it survives the small distortions a beam picks up along the way. This makes skyrmions promising carriers of information for optical communication and computing.[^protection]<sup>,</sup>[^arithmetic]

Optical devices that reshape such patterns are usually built for one job: one pattern in, one pattern out. We designed a single passive device that does three. Send in one pattern and out comes a second; send in another and out comes a different one, with no moving parts, no power and nothing to switch.

The device is a stack of three thin layers, each made of many pixels. Picture every polarisation state as a point on a sphere. The two outer layers rotate the sphere, moving all points together. The middle layer, a partial polariser, pulls the points towards one side and changes the distances between them. This is what lets each input go to an unrelated output, at the cost of absorbing some light. We showed that this stack can perform any three conversions exactly, and that three is the limit for any passive polarisation device: a fourth works only in special cases.

In simulations, one device turns three beams of uniform polarisation into skyrmions with skyrmion numbers 1, 5 and 10, and another converts skyrmions from one number to another. We also built converters in the laboratory, and their topological numbers came out within 0.06 of whole numbers. This work, with colleagues at the University of Oxford, has been accepted in *Nature Communications*.[^zhang]

### References

[^shen]: Shen, Y. *et al.* Optical skyrmions and other topological quasiparticles of light. *Nature Photonics* **18**, 15–25 (2024). [doi:10.1038/s41566-023-01325-7](https://doi.org/10.1038/s41566-023-01325-7)

[^protection]: Wang, A. A. *et al.* Topological protection of optical skyrmions through complex media. *Light: Science & Applications* **13**, 314 (2024). [doi:10.1038/s41377-024-01659-z](https://doi.org/10.1038/s41377-024-01659-z)

[^arithmetic]: Wang, A. A. *et al.* Perturbation-resilient integer arithmetic using optical skyrmions. *Nature Photonics* **19**, 1367–1375 (2025). [doi:10.1038/s41566-025-01779-x](https://doi.org/10.1038/s41566-025-01779-x)

[^zhang]: Zhang, R., Marozsak, T., Deng, L., Zhang, Y. *et al.* Multiplexed vector beam conversion via nonunitary spatial polarization transformation. *Nature Communications* (accepted, 2026). The first four authors contributed equally.
