import numpy as np
import matplotlib.pyplot as plt

# Datos de ISM para objetos con 4 filtros
data = {
    "BD+38 4058": {
        "B": {"q": 2.845, "σq": 0.91, "u": -0.818, "σu": 0.85},
        "V": {"q": 2.535, "σq": 0.62, "u": -4.833, "σu": 0.44},
        "R": {"q": 1.371, "σq": 0.41, "u": -0.408, "σu": 0.26},
        "I": {"q": 1.220, "σq": 0.44, "u": -3.109, "σu": 1.19},
    },
    "ATO J278.3657-10.5901": {
        "B": {"q": -4.303, "σq": 0.64, "u": 7.643, "σu": 0.52},
        "V": {"q": -3.082, "σq": 0.15, "u": 8.154, "σu": 0.46},
        "R": {"q": -2.028, "σq": 0.66, "u": 7.434, "σu": 1.39},
        "I": {"q": -1.647, "σq": 0.37, "u": 5.970, "σu": 1.16},
    },
    "NGC 6649 9": {
        "B": {"q": -3.144, "σq": 0.54, "u": 3.914, "σu": 0.56},
        "V": {"q": -2.529, "σq": 0.57, "u": 4.127, "σu": 0.49},
        "R": {"q": -1.676, "σq": 0.64, "u": 4.111, "σu": 0.52},
        "I": {"q": -1.120, "σq": 0.38, "u": 3.550, "σu": 0.27},
    }
}

plt.figure(figsize=(6,6))
markers = ['o','s','^']

# Dibujar Q–U para cada objeto
for (obj, filt_vals), m in zip(data.items(), markers):
    qs, us, sq, su = [], [], [], []
    for filt in ["B","V","R","I"]:
        v = filt_vals[filt]
        qs.append(v["q"]); us.append(v["u"])
        sq.append(v["σq"]); su.append(v["σu"])
    qs, us, sq, su = map(np.array, (qs, us, sq, su))
    plt.errorbar(qs, us, xerr=sq, yerr=su, fmt=m, capsize=3, label=obj)

# Ejes y cuadrícula
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.xlabel(r'$q_{\rm ISM}$ (%)')
plt.ylabel(r'$u_{\rm ISM}$ (%)')
plt.title('Diagrama Q–U de Polarización Interestelar')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
