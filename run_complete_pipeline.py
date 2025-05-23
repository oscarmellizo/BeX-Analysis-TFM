from StellarPolAnalyzer import run_complete_polarimetric_pipeline
import astropy.units as u
import sys
import os

standards = [
    {"path": "noche1_20230720_organize/BD+384058/BessellI/", "filter": "I", "snr": 70},
    {"path": "noche1_20230720_organize/BD+384058/BessellR/", "filter": "R", "snr": 35},
    {"path": "noche1_20230720_organize/BD+384058/JohnsonB/", "filter": "B", "snr": 40},
    {"path": "noche1_20230720_organize/BD+384058/JohnsonV/", "filter": "V", "snr": 0},
]

others = [
    {"path": "noche1_20230720_organize/1H1936+541/BessellI/", "filter": "I", "snr": 20},
    {"path": "noche1_20230720_organize/1H1936+541/BessellR/", "filter": "R", "snr": 0},
    {"path": "noche1_20230720_organize/1H1936+541/JohnsonV/", "filter": "V", "snr": 0},
    {"path": "noche1_20230720_organize/EXO2030+375/BessellI/", "filter": "I", "snr": 130},
    {"path": "noche1_20230720_organize/EXO2030+375/BessellR/", "filter": "R", "snr": 40},
    {"path": "noche1_20230720_organize/HD154892/BessellI/", "filter": "I", "snr": 0},
    {"path": "noche1_20230720_organize/HD154892/BessellR/", "filter": "R", "snr": 0},
    {"path": "noche1_20230720_organize/MWC656/BessellR/", "filter": "R", "snr": 0},
    {"path": "noche1_20230720_organize/MWC656/JohnsonB/", "filter": "B", "snr": 0},
    {"path": "noche1_20230720_organize/SS397/BessellI/", "filter": "I", "snr": 70},
    {"path": "noche1_20230720_organize/SS397/BessellR/", "filter": "R", "snr": 60},
    {"path": "noche1_20230720_organize/SS397/JohnsonB/", "filter": "B", "snr": 40},
    {"path": "noche1_20230720_organize/SS397/JohnsonV/", "filter": "V", "snr": 40},
    {"path": "noche1_20230720_organize/XMMJ183328/BessellI/", "filter": "I", "snr": 40},
    {"path": "noche1_20230720_organize/XMMJ183328/BessellR/", "filter": "R", "snr": 40},
    {"path": "noche1_20230720_organize/XMMJ183328/JohnsonB/", "filter": "B", "snr": 60},
    {"path": "noche1_20230720_organize/XMMJ183328/JohnsonV/", "filter": "V", "snr": 0},
]

for row in others:
    try:
        path = row["path"]
        entries = [f for f in os.listdir(path)
                    if os.path.isfile(os.path.join(path, f))]
    except FileNotFoundError:
        print(f"Error: la carpeta '{path}' no existe.")
        sys.exit(1)

    if len(entries) != 4:
        print(f"Error: se esperaban 4 archivos en '{path}', pero se encontraron {len(entries)}.")
        sys.exit(1)

    # Orden alfabético 
    entries.sort()

    # Construir rutas completas
    ref = os.path.join(path, entries[0])
    others = [os.path.join(path, fn) for fn in entries[1:]]

    print(ref)
    print(others)

    angles = [0.0, 22.5, 45.0, 67.5]
    image_paths, polar, wcs, enriched = run_complete_polarimetric_pipeline(
        ref, others, angles, row["filter"],
        fwhm=3.0, threshold_multiplier=5.0,
        tol_distance=1.44, tol_angle=1.2, max_distance=50,
        phot_aperture_radius=5, r_in=7, r_out=10, SNR_threshold=row["snr"],
        astrometry_api_key="gqvabohdmpdjuqlg",
        simbad_radius=0.01*u.deg,
        synthetic_name='synthetic_field.fits',
        save_plots=True,
        report_dir=path + "reports"
    )

    print('Imágenes procesadas:')
    for p in image_paths:
        print(' -', p)