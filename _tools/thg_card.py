"""Card image for the lipid droplet project (_projects/lipid-droplets.md).

Simulated 4π THG power of the 7.32 µm bead on the xz plane: the flood fill
stored by the thg_detection_7um_two_gaussians notebook in the Mathematica
repository (Mie, polystyrene in water; particle χ³ only, host ratio 0).
Linear grayscale on black, true aspect ratio, cropped to a square around the
bright region and smoothly interpolated.

Run with the Mathematica repository's own Python (it loads the stored flood
with that repository's code):
    /Users/marozsak/MIT/Developer/Mathematica/.venv/bin/python _tools/thg_card.py \
        assets/img/projects/lipid-droplets.png

Jekyll ignores this folder (leading underscore), so it is not published.
"""
import argparse
import sys
from pathlib import Path

import numpy as np

MATHEMATICA = Path("/Users/marozsak/MIT/Developer/Mathematica/nonlinear_mie_scattering")


def load_plane(plane, catalog, ratio, diameter_um=7.32, wavelength_um=1.1):
    """(h, z, P) of the stored flood on one plane, as the notebook's Simulation view shows it."""
    sys.path.insert(0, str(MATHEMATICA / "scripts"))
    import thg_detection.chi_basis_catalog as chi_basis
    from thg_detection.host_chi3_view import unfolded_plane
    from thg_detection.materials import catalog_indices
    from thg_evaluators.mie_points import mie_spec

    idx = catalog_indices(wavelength_um, catalog)
    n_host_3w = float(idx["n_host_3w"])
    spec = mie_spec(
        diameter=diameter_um * 1e-6, vacuum_wavelength=wavelength_um * 1e-6,
        n_sphere_w=idx["n_sphere_w"], n_sphere_3w=idx["n_sphere_3w"],
        n_host_w=idx["n_host_w"], n_host_3w=n_host_3w,
        chi3_xxxx=10.0 ** (-21.69897), e0=10.0 ** 8.0,
        excitation_na=1.05, collection_na=n_host_3w, symmetry="mirror_xy",
    )
    store = chi_basis.ChiBasisStore(MATHEMATICA / "results" / "thg_detection_7um_two_gaussians")
    table = chi_basis.load_basis(store, spec).at_ratio(ratio)
    h, z, p = unfolded_plane(table, plane)
    return np.asarray(h) * 1e6, np.asarray(z) * 1e6, np.asarray(p)


def render(out, h, z, p, half_width, size, gamma):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ph = np.min(np.diff(np.unique(np.round(h, 4))))
    pz = np.min(np.diff(np.unique(np.round(z, 4))))
    ih, iz = np.rint(h / ph).astype(int), np.rint(z / pz).astype(int)
    image = np.zeros((iz.max() - iz.min() + 1, ih.max() - ih.min() + 1))   # unsolved voxels: black
    image[iz - iz.min(), ih - ih.min()] = (p / p.max()) ** gamma
    extent = [h.min() - ph / 2, h.max() + ph / 2, z.min() - pz / 2, z.max() + pz / 2]

    fig = plt.figure(figsize=(size / 100, size / 100), dpi=100, facecolor="black")
    ax = fig.add_axes([0, 0, 1, 1], facecolor="black")
    ax.imshow(image, cmap="gray", vmin=0, vmax=1, origin="lower", extent=extent,
              interpolation="bicubic", aspect="equal")
    # Centre the square on the bright region (above 5% of the peak).
    bright = p > 0.05 * p.max()
    hc = 0.5 * (h[bright].min() + h[bright].max())
    zc = 0.5 * (z[bright].min() + z[bright].max())
    ax.set_xlim(hc - half_width, hc + half_width)
    ax.set_ylim(zc - half_width, zc + half_width)
    ax.set_axis_off()
    fig.savefig(out, dpi=100, facecolor="black")
    plt.close(fig)


if __name__ == "__main__":
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("out", help="output PNG")
    a.add_argument("--plane", default="xz", choices=("xz", "yz"))
    a.add_argument("--catalog", default="mie", help="mie (polystyrene in water) or green_mie (all water)")
    a.add_argument("--ratio", type=float, default=0.0, help="host χ³ / particle χ³")
    a.add_argument("--half-width", type=float, default=8.5, help="half the square's side, in µm")
    a.add_argument("--gamma", type=float, default=1.0, help="1 = linear grayscale")
    a.add_argument("--size", type=int, default=400, help="image size in px")
    args = a.parse_args()
    h, z, p = load_plane(args.plane, args.catalog, args.ratio)
    render(args.out, h, z, p, args.half_width, args.size, args.gamma)
