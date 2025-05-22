import numpy as np
import matplotlib.pyplot as plt

# Efective wavelengths (μm)
wavelengths = np.array([0.44, 0.55, 0.65, 0.80])

# Parámetros q_ISM ± σq y u_ISM ± σu para cada objeto y filtro
data = {
    "BD+38 4058": {
        "B": {"q": 2.845, "σq": 0.91, "u": -0.818, "σu": 0.85},
        "V": {"q": 2.535, "σq": 0.62, "u": -4.833, "σu": 0.44},
        "R": {"q": 1.371, "σq": 0.41, "u": -0.408, "σu": 0.26},
        "I": {"q": 1.220, "σq": 0.44, "u": -3.109, "σu": 1.19},
    },
    "ATO J278.3657-10.5901": {
        "B": {"q": -4.303, "σq": 0.64, "u": 7.643, "σu": 0.52},
        "V": {"q": -3.082, "σq": 0.15, "u": 8.154, "σu": 0.46},
        "R": {"q": -2.028, "σq": 0.66, "u": 7.434, "σu": 1.39},
        "I": {"q": -1.647, "σq": 0.37, "u": 5.970, "σu": 1.16},
    },
    "NGC 6649 9": {
        "B": {"q": -3.144, "σq": 0.54, "u": 3.914, "σu": 0.56},
        "V": {"q": -2.529, "σq": 0.57, "u": 4.127, "σu": 0.49},
        "R": {"q": -1.676, "σq": 0.64, "u": 4.111, "σu": 0.52},
        "I": {"q": -1.120, "σq": 0.38, "u": 3.550, "σu": 0.27},
    }
}

plt.figure(figsize=(8, 5))
for obj, filt_vals in data.items():
    P_vals = []
    σP_vals = []
    # Ordenar filtros según wavelengths
    for wl, filt in zip(wavelengths, ["B","V","R","I"]):
        vals = filt_vals[filt]
        q, σq, u, σu = vals["q"], vals["σq"], vals["u"], vals["σu"]
        # Polarización y error
        P = np.hypot(q, u)
        σP = np.sqrt((q*σq/P)**2 + (u*σu/P)**2)
        P_vals.append(P)
        σP_vals.append(σP)
    plt.errorbar(wavelengths, P_vals, yerr=σP_vals,
                 marker='o', linestyle='-', capsize=3, label=obj)

plt.xlabel('Longitud de onda λ (µm)')
plt.ylabel('Polarización interestelar P_ISM (%)')
plt.title('Dependencia espectral de la polarización interestelar para objetos con 4 filtros')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
