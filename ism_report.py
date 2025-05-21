import json
import os
import pandas as pd

def build_ism_summary(paths):
    """
    Construye un DataFrame resumen de ISM a partir de directorios que contienen
    '' y 'ism_estimation.json'.

    Columnas resultantes:
      - Object        : simbad_id del 
      - q_ISM ± σ     : valor de q_ISM y su sigma según dominant_q
      - u_ISM ± σ     : valor de u_ISM y su sigma según dominant_u
      - Dominant q    : índice de componente dominante para q
      - Dominant u    : índice de componente dominante para u
    """
    rows = []
    for path in paths:
        pfile = os.path.join(path, "")
        print(pfile)
        
        
        ifile = os.path.join(path, "ism_estimation.json")
        # Cargar JSONs
        with open(pfile, 'r', encoding='utf-8') as f:
            pipeline = json.load(f)
        with open(ifile, 'r', encoding='utf-8') as f:
            ism = json.load(f).get("ism_estimation", {})
        # Extraer simbad_id
        obj = pipeline.get("simbad_id")
        # Índices dominantes
        dq = ism.get("dominant_q", 0)
        du = ism.get("dominant_u", 0)
        # Listas de valores
        q_means   = ism.get("q_means", [])
        q_sigmas  = ism.get("q_sigmas", [])
        u_means   = ism.get("u_means", [])
        u_sigmas  = ism.get("u_sigmas", [])
        # Seleccionar componente dominante si existe
        try:
            q_val   = q_means[dq]
            q_err   = q_sigmas[dq]
            q_field = f"{q_val:.3f} ± {q_err:.3f}"
        except Exception:
            q_field = "-"
        try:
            u_val   = u_means[du]
            u_err   = u_sigmas[du]
            u_field = f"{u_val:.3f} ± {u_err:.3f}"
        except Exception:
            u_field = "-"
        # Agregar fila
        rows.append({
            "Object":       obj,
            "q_ISM ± σ":    q_field,
            "u_ISM ± σ":    u_field,
            "Dominant q":   dq,
            "Dominant u":   du,
            "path": path
        })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    import sys
    # Pasar los paths como argumentos de línea de comandos
    paths = [
        'noche1_20230720_organize/1H1936+541/BessellI/reports/',
        'noche1_20230720_organize/1H1936+541/BessellR/reports/',
        'noche1_20230720_organize/1H1936+541/JohnsonV/reports/',
        'noche1_20230720_organize/BD+384058/BessellI/reports/',
        'noche1_20230720_organize/BD+384058/BessellR/reports/',
        'noche1_20230720_organize/BD+384058/JohnsonB/reports/',
        'noche1_20230720_organize/BD+384058/JohnsonV/reports/',
        'noche1_20230720_organize/EXO2030+375/BessellI/reports/',
        'noche1_20230720_organize/EXO2030+375/BessellR/reports/',
        'noche1_20230720_organize/HD154892/BessellI/reports/',
        'noche1_20230720_organize/HD154892/BessellR/reports/',
        'noche1_20230720_organize/MWC656/BessellR/reports/',
        'noche1_20230720_organize/MWC656/JohnsonB/reports/',
        'noche1_20230720_organize/SS397/BessellI/reports/',
        'noche1_20230720_organize/SS397/BessellR/reports/',
        'noche1_20230720_organize/SS397/JohnsonB/reports/',
        'noche1_20230720_organize/SS397/JohnsonV/reports/',
        'noche1_20230720_organize/XMMJ183328/BessellI/reports/',
        'noche1_20230720_organize/XMMJ183328/BessellR/reports/',
        'noche1_20230720_organize/XMMJ183328/JohnsonB/reports/',
        'noche1_20230720_organize/XMMJ183328/JohnsonV/reports/'
    ]
    df_summary = build_ism_summary(paths)
    # Mostrar como tabla Markdown
    print(df_summary.to_markdown(index=False))
