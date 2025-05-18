from StellarPolAnalyzer import run_complete_polarimetric_pipeline
from StellarPolAnalyzer.organize import organize_night_images
import astropy.units as u
import traceback
import os

# Primero organizamos las imágenes de la noche
groups = organize_night_images(
    night_dir="noche1_20230720",
    output_base="noche1_20230720_organize"
)

for grp in groups:
    # Creamos el directorio de reports si no existe
    report_dir = grp["group_dir"] / "reports"
    os.makedirs(report_dir, exist_ok=True)

    # Ruta del fichero de log de errores
    log_path = report_dir / "error_log.txt"

    # Preparamos los paths para el pipeline
    final_paths = [grp["paths"][ang] for ang in grp["angles"]]
    ref = str(final_paths[0])
    others = [str(p) for p in final_paths[1:]]
    
    try:
        print(f"Procesando Target={grp['target']}  Filter={grp['filter']} …")
        image_paths, polar, wcs, enriched = run_complete_polarimetric_pipeline(
            ref_path=ref,
            other_paths=others,
            pol_angles=grp["angles"],
            fwhm=3.0, threshold_multiplier=5.0,
            tol_distance=1.44, tol_angle=1.2, max_distance=75,
            phot_aperture_radius=5, r_in=7, r_out=10, SNR_threshold=0,
            astrometry_api_key="gqvabohdmpdjuqlg",
            simbad_radius=0.01*u.deg,
            synthetic_name='synthetic_field.fits',
            save_plots=True,
            report_dir=str(report_dir)
        )
        print('→ Imágenes procesadas:')
        for p in image_paths:
            print('   -', p)

    except Exception as e:
        # Capturamos la traza completa
        tb = traceback.format_exc()
        # Escribimos en el log
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"ERROR en Target={grp['target']}  Filter={grp['filter']}\n")
            log.write(f"{tb}\n")
            log.write("-" * 80 + "\n")
        print(f"¡Error procesando {grp['target']} / {grp['filter']}, ver {log_path}!")        
        # Continuamos con el siguiente grupo
        continue
