from StellarPolAnalyzer import run_complete_polarimetric_pipeline
import astropy.units as u
import sys
import os

folder_init = "noche1_20230720_organize/XMMJ183328/JohnsonV/"

try:
    entries = [f for f in os.listdir(folder_init)
                if os.path.isfile(os.path.join(folder_init, f))]
except FileNotFoundError:
    print(f"Error: la carpeta '{folder_init}' no existe.")
    sys.exit(1)

if len(entries) != 4:
    print(f"Error: se esperaban 4 archivos en '{folder_init}', pero se encontraron {len(entries)}.")
    sys.exit(1)

# Orden alfabético 
entries.sort()

# Construir rutas completas
ref = os.path.join(folder_init, entries[0])
others = [os.path.join(folder_init, fn) for fn in entries[1:]]

print(ref)
print(others)

angles = [0.0, 22.5, 45.0, 67.5]
image_paths, polar, wcs, enriched = run_complete_polarimetric_pipeline(
    ref, others, angles,
    fwhm=3.0, threshold_multiplier=5.0,
    tol_distance=1.44, tol_angle=1.2, max_distance=50,
    phot_aperture_radius=5, r_in=7, r_out=10, SNR_threshold=50,
    astrometry_api_key="gqvabohdmpdjuqlg",
    simbad_radius=0.01*u.deg,
    synthetic_name='synthetic_field.fits',
    save_plots=True,
    report_dir=folder_init + "reports"
)

print('Imágenes procesadas:')
for p in image_paths:
    print(' -', p)