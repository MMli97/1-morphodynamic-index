import matplotlib
matplotlib.use("Agg")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from style import apply_style

apply_style()

# Real classification results across versions
data = {
    "system": [
        "Eukaryotic cell", "Thermostat", "NYSE", "Adaptive immunity",
        "Catholic Church", "Fifth Republic", "Multicellular org.",
        "Authoritarian regime", "Supply chain", "Apple Inc.",
        "TikTok", "Static LLM", "Linux", "Reformed order",
        "Theor. physics"
    ],
    "V1": [
        "F01", "F05", "F03", "F01",
        "F04", "F01", "F04",
        "F05", "F03", "F01",
        "F01", "F04", "F01", "F04",
        "F01"
    ],
    "V2": [
        "F01", "F05", "F03", "F01",
        "F04", "F01", "F04",
        "F05", "F03", "F01",
        "F01", "F04", "F01", "F04",
        "F01"
    ],
    "V2.1.1": [
        "F01", "F05", "F03", "F01",
        "F04", "F01", "F04",
        "F05", "F03", "F01",
        "F01", "F04", "F01", "F04",
        "F01"
    ],
    "V2.1.2": [
        "F01", "F05", "F03", "F01",
        "F04", "F01", "F04",
        "F05", "F03", "F01",
        "F01", "F04", "F01", "F04",
        "F01"
    ],
}

df = pd.DataFrame(data).set_index("system")

# Create numeric encoding for color
all_regimes = sorted(set(df.values.flatten()))
regime_to_num = {r: i for i, r in enumerate(all_regimes)}
df_num = df.apply(lambda col: col.map(regime_to_num))

plt.figure(figsize=(9, 7))

sns.heatmap(
    df_num,
    annot=df.values,
    fmt="",
    cmap="viridis",
    cbar=False,
    linewidths=0.5,
    linecolor="white",
)

plt.title("Evolution of the classification instrument across versions")
plt.ylabel("")
plt.tight_layout()

plt.savefig("classifier_heatmap.pdf", dpi=150)
plt.savefig("classifier_heatmap.png", dpi=150)
print("Saved classifier_heatmap.pdf/.png")
