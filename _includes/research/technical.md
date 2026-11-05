{%- comment -%}
  Technical version of /research/ (for fellow scientists). Markdown.
  Citations: [^t-name] after a sentence, [^t-name]: ... at the bottom.
  Maths (KaTeX): inline $$x$$ inside a sentence; display maths as $$...$$ in its own paragraph.
{%- endcomment -%}
## Differentiable modelling for quantitative THG microscopy

I am developing a differentiable electromagnetic framework for predicting and fitting THG microscope scans of spherical particles in nonlinear media. The objective is to distinguish particle size and material response from illumination and collection effects, supporting quantitative measurements of controlled beads and, ultimately, approximately spherical lipid droplets.[^t-debarre]

Green-function formulations established how focused excitation and coherent source interference determine THG image contrast.[^t-cheng] Subsequent FDTD studies demonstrated that local refractive-index discontinuities can distort the excitation field sufficiently to alter experimental images substantially.[^t-morizet] Nonlinear Mie theories have also characterised multipolar harmonic emission from spherical particles.[^t-smirnova] My work combines focused nonlinear-sphere scattering, an unbounded nonlinear host, and parameter derivatives within a framework designed for complete scan prediction and inverse fitting.

The solver represents the fields in vector spherical waves and expands a translated Debye–Wolf excitation field about the particle. The linear Mie response determines the pump field, which drives a prescribed nonlinear polarization under the undepleted-pump approximation. For isotropic media,

$$
\mathbf{P}^{(3)}(3\omega)\propto\chi^{(3)}\left(\mathbf{E}_{\omega}\!\cdot\!\mathbf{E}_{\omega}\right)\mathbf{E}_{\omega}.
$$

Reciprocity with the sphere’s linear response at $$3\omega$$ maps the source onto outgoing electric- and magnetic-type multipoles. Detector-weighted angular powers then give the predicted scan signal.

The nonlinear-host calculation includes polarization driven by the total incident-plus-scattered pump throughout the exterior, retaining coherent interference between particle and host emission. Near-field quadrature and complex-contour integration treat the unbounded exterior source. Reverse-mode differentiation of the discretized model provides sensitivities for gradient-based fitting.

The simulation and fitting framework is implemented; experimental validation is underway using bead measurements. Current investigations concern size recovery and the distinguishability of refractive index, pupil aberrations, and angular collection parameters. Measurements under multiple conditions may help separate these effects, but reliable experimental recovery remains to be established. The broader aim is to determine when THG scans constrain physical properties, where ambiguities persist, and which acquisition conditions provide the missing information.

### References

[^t-debarre]: Débarre, D. *et al.* Imaging lipid bodies in cells and tissues using third-harmonic generation microscopy. *Nature Methods* **3**, 47–53 (2006). [doi:10.1038/nmeth813](https://doi.org/10.1038/nmeth813)

[^t-cheng]: Cheng, J.-X. & Xie, X. S. Green’s function formulation for third-harmonic generation microscopy. *Journal of the Optical Society of America B* **19**, 1604–1610 (2002). [doi:10.1364/JOSAB.19.001604](https://doi.org/10.1364/JOSAB.19.001604)

[^t-morizet]: Morizet, J. *et al.* Modeling nonlinear microscopy near index-mismatched interfaces. *Optica* **8**, 944–951 (2021). [doi:10.1364/OPTICA.421257](https://doi.org/10.1364/OPTICA.421257)

[^t-smirnova]: Smirnova, D. A. *et al.* Multipolar third-harmonic generation driven by optically induced magnetic resonances. *ACS Photonics* **3**, 1468–1476 (2016). [doi:10.1021/acsphotonics.6b00036](https://doi.org/10.1021/acsphotonics.6b00036)
