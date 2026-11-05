{%- comment -%}
  Introductory version of /research/ (for a general audience). Markdown.
  Citations: [^name] after a sentence, [^name]: ... at the bottom; numbered automatically.
  Footnote names must not clash with technical.md (that file prefixes its names with t-).
{%- endcomment -%}
## Third-harmonic generation for lipid droplet imaging

Cells continually balance storing energy with using it. Part of that balance takes place in *lipid droplets*: small compartments that hold reserves of fat. Found in animals, plants and fungi alike, these droplets release fatty acids that cells can draw on for energy and for building membranes as their needs change.

The amount of stored fat tells only part of the story. How it is distributed among droplets, and how their sizes change, can reveal how cells organise and mobilise their reserves. Droplet size is linked to the pathways cells use to break down stored fat: in liver cells, larger droplets are targeted by enzymes that break down fat at the droplet surface (lipolysis), whereas only smaller droplets are engulfed and digested by autophagy (lipophagy).[^schott] Following these changes could help us understand how cells respond to shifting energy demands, and how fat accumulates when metabolism is disrupted.

To study these processes, we want to follow droplets over time in living cells and tissues. *Third-harmonic generation (THG) microscopy* can image them without adding fluorescent labels.[^debarre] When a laser is tightly focused into the sample, it generates light at three times the incoming frequency: a different colour that the microscope can detect. This signal arises mainly where optical properties change on the scale of the focus, so lipid droplets, which differ sharply from their surroundings, stand out clearly. With polarised light, THG can even tell apart droplets that store different kinds of fat.[^bautista]

But seeing a droplet is not the same as measuring it. The droplet itself bends and reshapes the focused light. Light generated inside and around it can add up or cancel out, and the microscope collects only part of what emerges. The signal also depends on how the droplet's size compares with the focus, and that dependence shifts when the focus is made tighter or looser.[^debarre2005] Together, these effects can change how bright a droplet appears and how large it looks, which complicates interpreting the image.[^morizet] Yet droplet sizes are often read directly from the image: in one study, two standard analysis methods applied to the same THG images gave somewhat different average diameters.[^pajic]

I am developing a computational model that follows these interactions from illumination to detection. The aim is to work backwards from an image to a particle's size and optical properties, while accounting for the microscope's influence. Because changing the focus changes how the signal depends on size, imaging the same droplet under several focusing conditions may help separate its true size from these effects. The simulation framework is in place, and I am now validating it against experimental measurements of beads. This provides a controlled foundation for the longer-term goal: reliable, label-free measurements of approximately spherical lipid droplets.

### References

[^schott]: Schott, M. B. *et al.* Lipid droplet size directs lipolysis and lipophagy catabolism in hepatocytes. *Journal of Cell Biology* **218**, 3320–3335 (2019). [doi:10.1083/jcb.201803153](https://doi.org/10.1083/jcb.201803153)

[^debarre]: Débarre, D. *et al.* Imaging lipid bodies in cells and tissues using third-harmonic generation microscopy. *Nature Methods* **3**, 47–53 (2006). [doi:10.1038/nmeth813](https://doi.org/10.1038/nmeth813)

[^bautista]: Bautista, G. *et al.* Polarized THG microscopy identifies compositionally different lipid droplets in mammalian cells. *Biophysical Journal* **107**, 2230–2236 (2014). [doi:10.1016/j.bpj.2014.10.009](https://doi.org/10.1016/j.bpj.2014.10.009)

[^debarre2005]: Débarre, D., Supatto, W. & Beaurepaire, E. Structure sensitivity in third-harmonic generation microscopy. *Optics Letters* **30**, 2134 (2005). [doi:10.1364/OL.30.002134](https://doi.org/10.1364/OL.30.002134)

[^morizet]: Morizet, J. M. *et al.* Modeling nonlinear microscopy near index-mismatched interfaces. *Optica* **8**, 944–951 (2021). [doi:10.1364/OPTICA.421257](https://doi.org/10.1364/OPTICA.421257)

[^pajic]: Pajić, T. *et al.* Label-free third harmonic generation imaging and quantification of lipid droplets in live filamentous fungi. *Scientific Reports* **12**, 18760 (2022). [doi:10.1038/s41598-022-23502-4](https://doi.org/10.1038/s41598-022-23502-4)
