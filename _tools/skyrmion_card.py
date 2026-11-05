"""Card image for the vector beam multiplexing project (_projects/polarization-multiplexing.md).

A smoothly warped optical skyrmion drawn as polarization ellipses on a dark
background, in the colouring of the paper's figures (PlotGen.plotEllipisoid
with hue=True in the Oxford project code):
    hue        polarization azimuth, (atan2(s2, s1) + pi) / (2 pi)
    lightness  ellipticity, 0.5 + 2 chi / pi (one circular state white, the
               other dark; --lift raises the dark one so it shows on black)

Field: a Neel-type Stokes skyrmion with skyrmion number n. Its coordinates are
warped by a few long-wavelength waves and its azimuth twisted with radius.
These are smooth deformations, so it is still a skyrmion of number n.

The current image was made with (needs numpy and matplotlib):
    python _tools/skyrmion_card.py assets/img/projects/polarization-multiplexing.png

Jekyll ignores this folder (leading underscore), so it is not published.
"""
import argparse

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def hls_to_rgb(h, l, s):
    """Vectorised colorsys.hls_to_rgb."""
    c = (1 - np.abs(2 * l - 1)) * s
    hp = (h % 1) * 6
    x = c * (1 - np.abs(hp % 2 - 1))
    z = np.zeros_like(h)
    k = np.floor(hp).astype(int) % 6
    r = np.choose(k, [c, x, z, z, x, c])
    g = np.choose(k, [x, c, c, x, z, z])
    b = np.choose(k, [z, z, x, c, c, x])
    m = l - c / 2
    return np.stack([r + m, g + m, b + m], axis=-1)


def skyrmion(x, y, n, seed, twist, warp, core):
    """Normalized Stokes field (s1, s2, s3) of a warped, twisted skyrmion."""
    rng = np.random.default_rng(seed)
    u, v = x.copy(), y.copy()
    for _ in range(4):
        kx, ky = rng.normal(0, 1.6, 2)
        phase = rng.uniform(0, 2 * np.pi, 2)
        amp = warp * rng.uniform(0.5, 1.0)
        u += amp * np.sin(kx * x + ky * y + phase[0])
        v += amp * np.sin(ky * x - kx * y + phase[1])
    r, theta = np.hypot(u, v), np.arctan2(v, u)
    s3 = -np.cos(np.pi * np.clip(r, 0, 1) ** core)   # -1 at the core, +1 from r = 1 out
    azimuth = n * theta + twist * r ** 1.5
    rho = np.sqrt(np.clip(1 - s3 ** 2, 0, 1))
    return rho * np.cos(azimuth), rho * np.sin(azimuth), s3


def render(out, n, seed, twist, warp, core, extent, grid, scale, lw, lift, size, bg):
    c = np.linspace(-extent, extent, grid)
    x, y = np.meshgrid(c, -c)
    s1, s2, s3 = skyrmion(x, y, n, seed, twist, warp, core)

    psi = np.arctan2(s2, s1) / 2                       # ellipse orientation
    chi = np.arcsin(np.clip(s3, -1, 1)) / 2            # ellipticity angle
    hue = (np.arctan2(s2, s1) + np.pi) / (2 * np.pi)
    light = lift + (1 - lift) * (0.5 + 2 * chi / np.pi)
    rgb = hls_to_rgb(hue, light, np.ones_like(hue))

    cell = c[1] - c[0]
    t = np.linspace(0, 2 * np.pi, 48)
    segments, colours = [], []
    for i in range(grid):
        for j in range(grid):
            a, b = scale * cell * np.cos(chi[i, j]), scale * cell * np.sin(chi[i, j])
            ex, ey = a * np.cos(t), b * np.sin(t)
            cp, sp = np.cos(psi[i, j]), np.sin(psi[i, j])
            segments.append(np.column_stack([x[i, j] + cp * ex - sp * ey, y[i, j] + sp * ex + cp * ey]))
            colours.append(rgb[i, j])

    fig = plt.figure(figsize=(size / 100, size / 100), dpi=100, facecolor=bg)
    ax = fig.add_axes([0, 0, 1, 1], facecolor=bg)
    ax.add_collection(LineCollection(segments, colors=colours, linewidths=lw, capstyle="round"))
    lim = extent + 0.5 * cell
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.set_axis_off()
    fig.savefig(out, dpi=100, facecolor=bg)
    plt.close(fig)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("out", help="output PNG")
    p.add_argument("--n", type=int, default=3, help="skyrmion number")
    p.add_argument("--seed", type=int, default=8, help="random warp; change for a different shape")
    p.add_argument("--twist", type=float, default=2.0, help="spiral of the colour lobes")
    p.add_argument("--warp", type=float, default=0.16, help="strength of the warp")
    p.add_argument("--core", type=float, default=1.3, help="> 1 widens the coloured band")
    p.add_argument("--extent", type=float, default=0.72, help="half-width of the square, in skyrmion radii")
    p.add_argument("--grid", type=int, default=11, help="ellipses per row")
    p.add_argument("--scale", type=float, default=0.32, help="ellipse size, fraction of the grid spacing")
    p.add_argument("--lw", type=float, default=2.0, help="line width in points")
    p.add_argument("--lift", type=float, default=0.25, help="raises the dark polarization so it shows on black")
    p.add_argument("--size", type=int, default=400, help="image size in px")
    p.add_argument("--bg", default="#1a1a1a", help="background colour")
    a = p.parse_args()
    render(a.out, a.n, a.seed, a.twist, a.warp, a.core, a.extent, a.grid, a.scale, a.lw, a.lift, a.size, a.bg)
