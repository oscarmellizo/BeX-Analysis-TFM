from StellarPolAnalyzer import run_complete_polarimetric_pipeline
import astropy.units as u
import sys
import os

#folder_init = "noche1_20230720_organize/BD+384058/BessellI/"
#folder_init = "noche1_20230720_organize/BD+384058/BessellR/"
#folder_init = "noche1_20230720_organize/BD+384058/JohnsonB/"
#folder_init = "noche1_20230720_organize/BD+384058/JohnsonV/"

#folder_init = "noche1_20230720_organize/EXO2030+375/BessellI/"
#folder_init = "noche1_20230720_organize/EXO2030+375/BessellR/"

#folder_init = "noche1_20230720_organize/HD154892/BessellI/"
#folder_init = "noche1_20230720_organize/HD154892/BessellR/"

#folder_init = "noche1_20230720_organize/MWC656/BessellR/"
#folder_init = "noche1_20230720_organize/MWC656/JohnsonB/"

#folder_init = "noche1_20230720_organize/SS397/BessellI/"
#folder_init = "noche1_20230720_organize/SS397/BessellR/"
#folder_init = "noche1_20230720_organize/SS397/JohnsonB/"
#folder_init = "noche1_20230720_organize/SS397/JohnsonV/"

#folder_init = "noche1_20230720_organize/XMMJ183328/BessellI/"
#folder_init = "noche1_20230720_organize/XMMJ183328/BessellR/"
#folder_init = "noche1_20230720_organize/XMMJ183328/JohnsonB/"
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
    phot_aperture_radius=5, r_in=7, r_out=10, SNR_threshold=0,
    astrometry_api_key="gqvabohdmpdjuqlg",
    simbad_radius=0.01*u.deg,
    synthetic_name='synthetic_field.fits',
    save_plots=True,
    report_dir=folder_init + "reports"
)

print('Imágenes procesadas:')
for p in image_paths:
    print(' -', p)