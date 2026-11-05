{%- comment -%}
  Vector beam multiplexing, technical version (for fellow scientists). Markdown.
  Citations: [^t-name] after a sentence, [^t-name]: ... at the bottom.
  Maths (KaTeX): inline $$x$$ inside a sentence; display maths as $$...$$ in its own paragraph.
  No title here: both versions share the project's `heading` in _projects/polarization-multiplexing.md.
{%- endcomment -%}
Passive devices for vector-beam manipulation, from q-plates to metasurfaces, are usually designed to realize a single mapping from one fixed input field to one fixed output.[^t-rubin] Existing polarization-multiplexing schemes typically rely on orthogonal or otherwise predefined pairs of states, holography, or engineered noise.[^t-mueller]<sup>,</sup>[^t-cerjan]<sup>,</sup>[^t-xiong] In work accepted in *Nature Communications*,[^t-zhang] we formulate multichannel vector-beam conversion as an inverse-design problem for structured matter: find device parameters $$\mathbf{p}(\mathbf{r},\lambda)$$ such that a forward model $$f$$ carries each of $$N$$ prescribed input Stokes fields to its target,

$$\min_{\mathbf{p}} \; \sum_{i=1}^{N} \int \bigl\lVert f\bigl(\mathbf{p}(\mathbf{r},\lambda);\, \mathbf{S}^{\mathrm{in}}_i(\mathbf{r},\lambda)\bigr) - \mathbf{S}^{\mathrm{out}}_i(\mathbf{r},\lambda) \bigr\rVert^2 \, \mathrm{d}\mathbf{r}.$$

The mappings are local and evaluated at the exit plane, without free-space propagation or holographic reconstruction.[^t-shi] Wavelength dependence, platform-specific responses and imperfections can all enter through $$f$$. The realization studied here is a retarder–diattenuator–retarder (RDR) cascade: two arrays of elliptical retarders with arbitrary fast axes and retardances, on either side of a linear diattenuator with a fixed horizontal axis and a spatially varying transmission coefficient.

A pure polarization state is a Jones vector up to a complex scalar, a point of $$\mathbb{CP}^1$$ (the Poincaré sphere). Retarders act as rigid rotations of the sphere and preserve all angular distances, so a retarder-only device can realize several mappings only if the outputs are one rotation of the inputs. Diattenuation removes this obstruction. By singular value decomposition, any invertible Jones matrix, normalized by its largest singular value, takes the form

$$J = U \begin{pmatrix} 1 & 0 \\ 0 & \sigma \end{pmatrix} V^{\dagger}, \qquad 0 < \sigma \le 1,$$

with $$U$$ and $$V$$ unitary. The RDR cascade is therefore not an ansatz but the general form of a passive invertible polarization transformation.[^t-lu] Up to a scalar, such a map has six real degrees of freedom; a retarder and a fixed-axis diattenuator provide four, and the second retarder restores the rest, so with the diattenuator axis fixed the three-layer cascade is minimal. The factorization is not unique, because a retarder commuting with the diattenuator can be moved between layers. Neighbouring pixels optimized independently can settle on different, physically equivalent decompositions, which gives the parameter maps a granular appearance while the output fields remain continuous.

On states, $$J$$ acts as a Möbius transformation of $$\mathbb{CP}^1$$. Three prescribed channels $$a_i \mapsto b_i$$ can therefore be realized exactly if and only if the equality pattern is preserved: equal inputs go to equal outputs and distinct inputs to distinct outputs. For pairwise distinct inputs and outputs, the solution is unique up to a scalar and has a closed form. Writing $$A = [a_1\; a_2]$$, $$B = [b_1\; b_2]$$, $$a_3 = A\boldsymbol{\alpha}$$ and $$b_3 = B\boldsymbol{\beta}$$,

$$J \propto B \begin{pmatrix} \beta_1/\alpha_1 & 0 \\ 0 & \beta_2/\alpha_2 \end{pmatrix} A^{-1}.$$

Uniqueness means that $$\sigma$$, and with it the loss, is fixed by the task. $$\sigma = 1$$ only when the mapping is a rigid rotation, and $$\sigma \to 0$$ as two inputs approach each other while their targets stay apart: the diattenuator tends to a polarizer and the problem becomes ill-conditioned. For four channels, the first three pairs already determine $$J$$, so the fourth is realizable only if the cross-ratio is preserved,[^t-ahlfors]

$$\frac{\det[a_1\, a_3]\,\det[a_2\, a_4]}{\det[a_1\, a_4]\,\det[a_2\, a_3]} = \frac{\det[b_1\, b_3]\,\det[b_2\, b_4]}{\det[b_1\, b_4]\,\det[b_2\, b_3]}.$$

This is a measure-zero condition, so generic four-channel tasks have no exact solution. The limit of three independent channels per pixel is intrinsic to passive linear polarization transformations, not to the cascade or the optimizer. In 5,000 random tasks per channel count, two- and three-channel designs reached numerical precision, whereas four- and five-channel designs showed substantially larger errors.

Designs are obtained by minimizing the squared Stokes distance at every pixel with differential evolution from Latin-hypercube initializations,[^t-storn] which also accommodates parameter bounds, fabrication constraints and approximate solutions beyond three channels. For three channels, the closed form followed by an SVD gives the RDR parameters directly. On the 7,668 active pixels of one converter it reaches numerical precision everywhere, whereas 6.9% of the optimized pixels exceed a pixel error of $$10^{-4}$$, concentrated where the required transmission is low. In simulation, one device converts uniform 0° linear, 45° linear and right-circular inputs into Néel-type skyrmions with skyrmion numbers 1, 5 and 10; another converts skyrmions 1 → 5, 5 → 1 and 5 → −5 while preserving their boundary polarizations. With generalized skyrmion numbers,[^t-gsky] which assign a tuple of integers to fields without a uniform boundary, a third device converts right-circular polarization and skyrmions with skyrmion numbers +1 and +4 into fields with $$(-2, +1, +2)$$, $$(-1, +2, +3)$$ and $$(+2, +5, +6)$$. We implemented it experimentally with SLM-based meron retarders[^t-he] and a programmable diattenuator synthesized by an SLM between fixed-axis polarization optics. Across three experimental devices, the invariants evaluated from the measured pixel-wise Mueller matrices lie within 0.06 of integers.

The topological encoding also relaxes some practical requirements. Under a simplified fixed-thickness dispersion model, the skyrmion numbers of the generator stay within 0.5 of their design values over 100–200 nm, two to four times its 50 nm field-fidelity bandwidth. They are also stable under smooth input deviations, spatial coarse-graining, and quantization of the device parameters to 64 levels, whereas aperture truncation and lateral misalignment of structured inputs are more demanding. Open directions include a monolithic fixed-axis diattenuator with spatially varying strength (wire grids, dichroic films or metasurfaces), and wavelength as a further multiplexing dimension.

This is joint work at the University of Oxford, supervised by Chao He, with Runchen Zhang, Liangyu Deng and Yunqi Zhang as equal-contribution co-authors. I contributed to the concept and the numerical design, and developed the mathematical formulation with Liangyu Deng.

### References

[^t-rubin]: Rubin, N. A., Shi, Z. & Capasso, F. Polarization in diffractive optics and metasurfaces. *Advances in Optics and Photonics* **13**, 836–970 (2021). [doi:10.1364/AOP.439986](https://doi.org/10.1364/AOP.439986)

[^t-mueller]: Balthasar Mueller, J. P., Rubin, N. A., Devlin, R. C., Groever, B. & Capasso, F. Metasurface polarization optics: independent phase control of arbitrary orthogonal states of polarization. *Physical Review Letters* **118**, 113901 (2017). [doi:10.1103/PhysRevLett.118.113901](https://doi.org/10.1103/PhysRevLett.118.113901)

[^t-cerjan]: Cerjan, A. & Fan, S. Achieving arbitrary control over pairs of polarization states using complex birefringent metamaterials. *Physical Review Letters* **118**, 253902 (2017). [doi:10.1103/PhysRevLett.118.253902](https://doi.org/10.1103/PhysRevLett.118.253902)

[^t-xiong]: Xiong, B. *et al.* Breaking the limitation of polarization multiplexing in optical metasurfaces with engineered noise. *Science* **379**, 294–299 (2023). [doi:10.1126/science.ade5140](https://doi.org/10.1126/science.ade5140)

[^t-zhang]: Zhang, R., Marozsak, T., Deng, L., Zhang, Y. *et al.* Multiplexed vector beam conversion via nonunitary spatial polarization transformation. *Nature Communications* (accepted, 2026). The first four authors contributed equally.

[^t-shi]: Shi, Z., Rubin, N. A., Park, J.-S. & Capasso, F. Nonseparable polarization wavefront transformation. *Physical Review Letters* **129**, 167403 (2022). [doi:10.1103/PhysRevLett.129.167403](https://doi.org/10.1103/PhysRevLett.129.167403)

[^t-lu]: Lu, S.-Y. & Chipman, R. A. Homogeneous and inhomogeneous Jones matrices. *Journal of the Optical Society of America A* **11**, 766–773 (1994). [doi:10.1364/JOSAA.11.000766](https://doi.org/10.1364/JOSAA.11.000766)

[^t-ahlfors]: Ahlfors, L. V. *Complex Analysis*, 3rd edn, Ch. 3 (McGraw-Hill, 1979).

[^t-storn]: Storn, R. & Price, K. Differential evolution: a simple and efficient heuristic for global optimization over continuous spaces. *Journal of Global Optimization* **11**, 341–359 (1997). [doi:10.1023/A:1008202821328](https://doi.org/10.1023/A:1008202821328)

[^t-gsky]: Wang, A. A. *et al.* Redefining topological robustness in optical polarization fields through a generalized skyrmion number. *Nature Communications* **17**, 8539 (2026). [doi:10.1038/s41467-026-75120-7](https://doi.org/10.1038/s41467-026-75120-7)

[^t-he]: He, C. *et al.* A reconfigurable arbitrary retarder array as complex structured matter. *Nature Communications* **16**, 4902 (2025). [doi:10.1038/s41467-025-59846-4](https://doi.org/10.1038/s41467-025-59846-4)
