import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from style import apply_style, REGIME_COLORS

apply_style()

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(projection='3d')

# Axes: use the three primary gradients as conceptual axes
ax.set_xlabel(r"$\Delta_{23}$ (Prop. $-$ Integ.)", fontsize=10, labelpad=10)
ax.set_ylabel(r"$\Delta_{45}$ (Norm. $-$ Revis.)", fontsize=10, labelpad=10)
ax.set_zlabel(r"$\Delta_{12}$ (Depth $-$ Prop.)", fontsize=10, labelpad=10)

# Real system positions in gradient space
systems = {
    "Cell":       (-0.15, +0.30, +0.10, "F01"),
    "Thermostat": (-0.05, +0.50, -0.20, "F05"),
    "NYSE":       (+0.25, +0.10, -0.15, "F03"),
    "Immunity":   (-0.05, +0.10, +0.10, "F01"),
    "Church":     (-0.05, +0.65, +0.25, "F04"),
    "5th Rep.":   (+0.05, +0.20, +0.05, "F01"),
    "Organism":   (-0.10, +0.45, +0.15, "F04"),
    "Authorit.":  (+0.20, +0.75, +0.05, "F05"),
    "Supply ch.": (+0.35, +0.20, -0.25, "F03"),
    "Apple":      (-0.05, +0.20, +0.10, "F01"),
    "TikTok":     (+0.10, +0.10, -0.15, "F01"),
    "LLM":        (-0.20, +0.05, +0.35, "F04"),
    "Linux":      (-0.15, +0.05, +0.15, "F01"),
    "Ref. order": (-0.15, +0.45, +0.25, "F04"),
    "Physics":    (-0.10, -0.05, +0.15, "F01"),
}

# Plot each system
for name, (d23, d45, d12, regime) in systems.items():
    color = REGIME_COLORS.get(regime, "#666")
    ax.scatter(d23, d45, d12, c=color, s=60, edgecolors="white", linewidths=0.3, zorder=3)
    ax.text(d23, d45, d12 + 0.03, name, fontsize=7, color="#333")

# Origin lines
ax.plot([-0.4, 0.5], [0, 0], [0, 0], color="grey", linewidth=0.4, linestyle="--")
ax.plot([0, 0], [-0.2, 0.9], [0, 0], color="grey", linewidth=0.4, linestyle="--")
ax.plot([0, 0], [0, 0], [-0.3, 0.4], color="grey", linewidth=0.4, linestyle="--")

ax.set_title("Morphodynamic gradient space (V2.1.2)", fontsize=13)

# Legend
from matplotlib.lines import Line2D
legend_elems = [Line2D([0], [0], marker='o', color='w',
                       markerfacecolor=REGIME_COLORS[r], markersize=8, label=r)
                for r in ["F01", "F03", "F04", "F05"]]
ax.legend(handles=legend_elems, loc="upper left", fontsize=9, framealpha=0.9)

ax.view_init(elev=25, azim=-50)
plt.tight_layout()

plt.savefig("phase_space.pdf", dpi=150)
plt.savefig("phase_space.png", dpi=150)
print("Saved phase_space.pdf/.png")
