import os
import json
import numpy as np
import matplotlib.pyplot as plt

# Configuración
base_dir = "ruta/a/tus/datos"  # Cambia esto a la carpeta raíz donde están organizados los campos
fields = ["1H1936+541", "ATOJ278.3657-10.5901", "BD+384058", 
          "HD154892", "HD215227", "NGC66499", "V*V2246Cyg"]
filters = ["B", "V", "R", "I"]

#for filt in filters:
#    for field in fields:
field = "NGC  6649     9"
filt = "V"
# Paths a JSONs del pipeline y de ISM
pipeline_path = os.path.join("noche1_20230720_organize/XMMJ183328/Johnson" + filt +"/reports/pipeline_results.json")
ism_path      = os.path.join("noche1_20230720_organize/XMMJ183328/Johnson" + filt +"/reports/ism_estimation.json")

# Cargar datos
if not os.path.exists(pipeline_path):
    print("Error en path " + pipeline_path)
with open(pipeline_path, 'r', encoding='utf-8') as f:
    records = json.load(f)
if not os.path.exists(ism_path):
    print("Error en path " + ism_path)
with open(ism_path, 'r', encoding='utf-8') as f:
    ism = json.load(f)['ism_estimation']

# Extraer Q, U de todas las estrellas
q_all = np.array([rec['q'] for rec in records])
u_all = np.array([rec['u'] for rec in records])

# Estrella de interés
target = next((rec for rec in records if rec.get('simbad_id') == field), None)
q_t, u_t = (target['q'], target['u']) if target else (None, None)

# ISM
dom_q = ism['dominant_q']
dom_u = ism['dominant_u']
q_ism = ism['q_means'][dom_q]
u_ism = ism['u_means'][dom_u]

# Plot
plt.figure(figsize=(5,5))
plt.scatter(q_all, u_all, c='grey', alpha=0.6, s=20, label='Estrellas campo')
if q_t is not None:
    plt.scatter(q_t, u_t, c='red', s=80, label=field)
plt.scatter(q_ism, u_ism, c='black', marker='X', s=100, label='ISM')

plt.axhline(0, color='k', lw=0.5)
plt.axvline(0, color='k', lw=0.5)
plt.xlabel("q (%)")
plt.ylabel("u (%)")
plt.title(f"Diagrama Q–U — {field} — Filtro {filt}")
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()
