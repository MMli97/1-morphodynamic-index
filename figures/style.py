import matplotlib.pyplot as plt

REGIME_COLORS = {
    "F01": "#4C78A8",   # Differential equilibrium
    "F03": "#2F4B7C",   # Propagation crisis
    "F04": "#8F77B5",   # Inertial plateau
    "F05": "#E45756",   # Normative dominance
    "F06": "#F58518",   # Normative inversion
    "F08": "#9C755F",   # Functional dissolution
    "F09": "#BAB0AC",   # Pure architecture
}

def apply_style():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "figure.figsize": (8,6)
    })