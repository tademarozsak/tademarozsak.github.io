{%- comment -%}
  Technical version of /research/ (for fellow scientists). Markdown.
  Citations: [^t-name] after a sentence, [^t-name]: ... at the bottom.
  Maths (KaTeX): inline $$x$$ inside a sentence; display maths as $$...$$ in its own paragraph.
{%- endcomment -%}
## Differentiable modelling for quantitative THG microscopy

I am developing a differentiable electromagnetic framework for predicting and fitting THG microscope scans of spherical particles in nonlinear media. The objective is to distinguish particle size and material response from illumination and collection effects, supporting quantitative measurements of controlled beads and, ultimately, approximately spherical lipid droplets.[^t-debarre]

Green-function formulations established how focused excitation and coherent source interference determine THG image contrast.[^t-cheng] Experiments showed that the signal from a homogeneous sphere depends on its size relative to the focal volume, and that this dependence can be tuned through the excitation Rayleigh length.[^t-debarre2005] FDTD studies subsequently demonstrated that local refractive-index discontinuities can distort the excitation field sufficiently to alter experimental images substantially, including polarization-resolved contrast.[^t-morizet]<sup>,</sup>[^t-morizet2023] Nonlinear Mie theories have characterised multipolar THG from spherical particles, largely for plane-wave excitation, from micrometre-scale droplets[^t-kasparian] to resonant high-index nanoparticles.[^t-smirnova] Meanwhile, lipid-droplet diameters have been estimated from THG images by particle analysis and image correlation spectroscopy, without a model of image formation.[^t-pajic] My work combines focused nonlinear-sphere scattering, an unbounded nonlinear host, and parameter derivatives within a framework designed for complete scan prediction and inverse fitting.

The solver represents the fields in vector spherical waves and expands a translated Debye–Wolf excitation field about the particle. The linear Mie response determines the pump field, which drives a prescribed third-order polarization at $$3\omega$$ under the undepleted-pump approximation. Besides isotropic media, the source construction accepts a general rank-four $$\chi^{(3)}$$ tensor, relevant because lipid ordering can make droplets nonlinearly anisotropic;[^t-bautista] this anisotropic path is implemented but less extensively validated than the isotropic case. Reciprocity with the sphere’s linear response at $$3\omega$$ maps the source onto outgoing electric- and magnetic-type multipoles. Detector-weighted angular powers then give the predicted scan signal.

The nonlinear-host calculation includes polarization driven by the total incident-plus-scattered pump throughout the exterior, retaining coherent interference between particle and host emission. Near-field quadrature and complex-contour integration treat the unbounded exterior source. Reverse-mode differentiation of the discretized model provides sensitivities for gradient-based fitting.

The simulation and fitting framework is implemented and reproduces the homogeneous-medium Green-function result in the index-matched limit; experimental validation is underway using bead measurements. Current investigations concern size recovery and the distinguishability of refractive index, pupil aberrations, and angular collection parameters. Measurements under multiple focusing conditions may help separate these effects, but reliable experimental recovery remains to be established. The broader aim is to determine when THG scans constrain physical properties, where ambiguities persist, and which acquisition conditions provide the missing information.

### References

[^t-debarre]: Débarre, D. *et al.* Imaging lipid bodies in cells and tissues using third-harmonic generation microscopy. *Nature Methods* **3**, 47–53 (2006). [doi:10.1038/nmeth813](https://doi.org/10.1038/nmeth813)

[^t-cheng]: Cheng, J.-X. & Xie, X. S. Green’s function formulation for third-harmonic generation microscopy. *Journal of the Optical Society of America B* **19**, 1604–1610 (2002). [doi:10.1364/JOSAB.19.001604](https://doi.org/10.1364/JOSAB.19.001604)

[^t-debarre2005]: Débarre, D., Supatto, W. & Beaurepaire, E. Structure sensitivity in third-harmonic generation microscopy. *Optics Letters* **30**, 2134 (2005). [doi:10.1364/OL.30.002134](https://doi.org/10.1364/OL.30.002134)

[^t-morizet]: Morizet, J. M. *et al.* Modeling nonlinear microscopy near index-mismatched interfaces. *Optica* **8**, 944–951 (2021). [doi:10.1364/OPTICA.421257](https://doi.org/10.1364/OPTICA.421257)

[^t-morizet2023]: Morizet, J. M. *et al.* Third harmonic imaging contrast from tubular structures in the presence of index discontinuity. *Scientific Reports* **13**, 7850 (2023). [doi:10.1038/s41598-023-34528-7](https://doi.org/10.1038/s41598-023-34528-7)

[^t-kasparian]: Kasparian, J. *et al.* Angular dependences of third harmonic generation from microdroplets. *Physical Review Letters* **78**, 2952–2955 (1997). [doi:10.1103/PhysRevLett.78.2952](https://doi.org/10.1103/PhysRevLett.78.2952)

[^t-smirnova]: Smirnova, D. A. *et al.* Multipolar third-harmonic generation driven by optically induced magnetic resonances. *ACS Photonics* **3**, 1468–1476 (2016). [doi:10.1021/acsphotonics.6b00036](https://doi.org/10.1021/acsphotonics.6b00036)

[^t-pajic]: Pajić, T. *et al.* Label-free third harmonic generation imaging and quantification of lipid droplets in live filamentous fungi. *Scientific Reports* **12**, 18760 (2022). [doi:10.1038/s41598-022-23502-4](https://doi.org/10.1038/s41598-022-23502-4)

[^t-bautista]: Bautista, G. *et al.* Polarized THG microscopy identifies compositionally different lipid droplets in mammalian cells. *Biophysical Journal* **107**, 2230–2236 (2014). [doi:10.1016/j.bpj.2014.10.009](https://doi.org/10.1016/j.bpj.2014.10.009)
