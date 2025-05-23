import numpy as np
import matplotlib.pyplot as plt

# Longitudes de onda efectivas de los filtros (µm)
wavelengths = {'B': 0.44, 'V': 0.55, 'R': 0.65, 'I': 0.80}

# Datos de polarización observada (P_obs ± σ_P) para cada objeto y filtro
# Basados en los resultados del pipeline
data = {
    "1H1936+541": {
        'I': (3.837, 0.002),
        'R': (9.831, 0.002),
        'V': (3.594, 0.003),
    },
    "ATOJ278.3657-10.5901": {
        'I': (12.3584, 0.0084),
        'R': (14.4597, 0.0007),
        'B': (15.7549, 0.0005),
        'V': (15.6071, 0.0007),
    },
    "BD+384058": {
        'I': (4.2747, 0.0005),
        'R': (5.1804, 0.0007),
        'B': (5.9701, 0.0007),
        'V': (5.8380, 0.0007),
    },
    "HD154892": {
        'I': (4.2378, 0.0083),
        'R': (5.2508, 0.0063),
        'B': (5.0880, 0.0082),
    },
    "HD215227": {
        'R': (5.5255, 0.0086),
        'B': (5.5866, 0.0084),
    },
    "NGC66499": {
        'I': (8.3343, 0.0007),
        'R': (10.4533, 0.0008),
        'B': (11.7603, 0.0006),
        'V': (11.4118, 0.0008),
    },
    "V*V2246Cyg": {
        'I': (14.365, 0.002),
        'R': (17.159, 0.003),
        'B': (12.467, 0.003),
        'V': (14.411, 0.002),
    }
}

plt.figure(figsize=(8, 5))

for obj, filt_vals in data.items():
    # Ordenar por longitud de onda
    filt_sorted = sorted(filt_vals.keys(), key=lambda f: wavelengths[f])
    lam = np.array([wavelengths[f] for f in filt_sorted])
    P_obs = np.array([filt_vals[f][0] for f in filt_sorted])
    sigma_P = np.array([filt_vals[f][1] for f in filt_sorted])

    plt.errorbar(lam, P_obs, yerr=sigma_P,
                 marker='o', linestyle='-',
                 capsize=3, label=obj)

plt.xlabel('Longitud de onda λ (µm)')
plt.ylabel('Polarización observada P (%)')
plt.title('Dependencia espectral de la polarización observada')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
