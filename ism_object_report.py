import os
import json
import pandas as pd

def build_ism_summary(root_dir):
    """
    Recorre recursivamente root_dir buscando pares de archivos 
    pipeline_results.json e ism_estimation.json y construye un DataFrame resumen.
    """
    rows = []
    #for dirpath, dirnames, filenames in os.walk(root_dir):
        #if 'pipeline_results.json' in filenames and 'ism_estimation.json' in filenames:
    pfile = os.path.join(root_dir, 'pipeline_results.json')
    ifile = os.path.join(root_dir, 'ism_estimation.json')
    # Cargar JSONs
    try:
        pipeline = json.load(open(pfile, 'r', encoding='utf-8'))
        ism_data = json.load(open(ifile, 'r', encoding='utf-8')).get("ism_estimation", {})
    except Exception:
        print("error")
    # Extraer campos
    obj = pipeline.get("simbad_id", os.path.basename(root_dir))
    dq = ism_data.get("dominant_q", 0)
    du = ism_data.get("dominant_u", 0)
    # Seleccionar valor y error de la componente dominante
    def select_component(lst, idx):
        try:
            val = lst[idx]
            return val
        except Exception:
            return None
    q_means  = ism_data.get("q_means", [])
    q_sigmas = ism_data.get("q_sigmas", [])
    u_means  = ism_data.get("u_means", [])
    u_sigmas = ism_data.get("u_sigmas", [])
    q_val = select_component(q_means, dq)
    q_err = select_component(q_sigmas, dq)
    u_val = select_component(u_means, du)
    u_err = select_component(u_sigmas, du)
    q_field = f"{q_val:.3f} ± {q_err:.3f}" if isinstance(q_val, (int, float)) and isinstance(q_err, (int, float)) else "-"
    u_field = f"{u_val:.3f} ± {u_err:.3f}" if isinstance(u_val, (int, float)) and isinstance(u_err, (int, float)) else "-"
    rows.append({
        "Object":     obj,
        "q_ISM ± σ":  q_field,
        "u_ISM ± σ":  u_field,
        "Dominant q": dq,
        "Dominant u": du
    })
    return pd.DataFrame(rows)

# Ejemplo de uso:
if __name__ == "__main__":
    df = build_ism_summary('noche1_20230720_organize/1H1936+541/BessellI/reports')
    print(df.to_markdown(index=False))
