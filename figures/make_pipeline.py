import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from style import apply_style

apply_style()

fig, ax = plt.subplots(figsize=(12, 3))

boxes = [
    ("Input vector\n$(A_1, A_2, A_3, A_4, A_5)$", 0.10),
    ("Gradient computation\n$\\Delta_{23} = A_2 - A_3$\n$\\Delta_{45} = A_4 - A_5$\n$\\Delta_{12} = A_1 - A_2$", 0.35),
    ("Regime constraints\n(F01 .. F09)", 0.60),
    ("Constraint-distance\nclassifier\n$\\hat{F}(x) = \\arg\\min_F d_F(x)$", 0.85),
]

for text, x in boxes:
    ax.text(x, 0.5, text,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#666", lw=1.2),
            ha="center", va="center", fontsize=10)

for i in range(len(boxes) - 1):
    ax.annotate("",
                xy=(boxes[i + 1][1] - 0.08, 0.5),
                xytext=(boxes[i][1] + 0.08, 0.5),
                arrowprops=dict(arrowstyle="->", color="#333", lw=1.5))

ax.set_xlim(-0.02, 1.02)
ax.set_ylim(0.1, 0.9)
ax.axis("off")
ax.set_title("Classifier pipeline", fontsize=13, pad=15)

plt.tight_layout()
plt.savefig("classifier_pipeline.pdf", dpi=150, bbox_inches="tight")
plt.savefig("classifier_pipeline.png", dpi=150, bbox_inches="tight")
print("Saved classifier_pipeline.pdf/.png")
