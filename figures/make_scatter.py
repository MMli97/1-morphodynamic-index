import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from style import apply_style, REGIME_COLORS

apply_style()

# Real V2.1.2 data (central estimates from classifier battery)
systems = [
    ("Eukaryotic cell",       -0.15, +0.30, "F01"),
    ("Thermostat",            -0.05, +0.50, "F05"),
    ("NYSE",                  +0.25, +0.10, "F03"),
    ("Adaptive immunity",     -0.05, +0.10, "F01"),
    ("Catholic Church",       -0.05, +0.65, "F04"),
    ("Fifth Republic",        +0.05, +0.20, "F01"),
    ("Multicellular org.",    -0.10, +0.45, "F04"),
    ("Authoritarian regime",  +0.20, +0.75, "F05"),
    ("Supply chain",          +0.35, +0.20, "F03"),
    ("Apple Inc.",            -0.05, +0.20, "F01"),
    ("TikTok",                +0.10, +0.10, "F01"),
    ("Static LLM",            -0.20, +0.05, "F04"),
    ("Linux",                 -0.15, +0.05, "F01"),
    ("Reformed order",        -0.15, +0.45, "F04"),
    ("Theor. physics",        -0.10, -0.05, "F01"),
]

df = pd.DataFrame(systems, columns=["system", "d23", "d45", "regime"])

fig, ax = plt.subplots(figsize=(10, 7))

for r, g in df.groupby("regime"):
    ax.scatter(g.d23, g.d45,
               label=r,
               color=REGIME_COLORS.get(r, "#666"),
               s=100, zorder=3, edgecolors="white", linewidths=0.5)

for _, row in df.iterrows():
    ax.annotate(row.system,
                (row.d23, row.d45),
                textcoords="offset points",
                xytext=(6, 4),
                fontsize=8, color="#333")

ax.axhline(0, color="grey", linewidth=0.5, linestyle="--")
ax.axvline(0, color="grey", linewidth=0.5, linestyle="--")

# Grey zone F01/F03
ax.axvspan(0.18, 0.23, alpha=0.08, color="orange", label="F01/F03 grey zone")

# Regime boundary hints
ax.axhline(0.40, color="#E45756", linewidth=0.7, linestyle=":", alpha=0.5)
ax.axhline(0.05, color="#F58518", linewidth=0.7, linestyle=":", alpha=0.5)

ax.set_xlabel(r"$\Delta_{23}$ (Propagation $-$ Integration)")
ax.set_ylabel(r"$\Delta_{45}$ (Normativity $-$ Revision)")
ax.set_title("Distribution of systems in gradient space (V2.1.2)")

ax.legend(title="Regime classification", loc="upper left", framealpha=0.9)
plt.tight_layout()

plt.savefig("scatter_gradient_space.pdf", dpi=150)
plt.savefig("scatter_gradient_space.png", dpi=150)
print("Saved scatter_gradient_space.pdf/.png")
