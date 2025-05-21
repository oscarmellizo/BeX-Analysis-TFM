# Primero organizamos las imágenes de la noche
from StellarPolAnalyzer.organize import organize_night_images

groups = organize_night_images(
    night_dir="noche1_20230720",
    output_base="noche1_20230720_organize"
)

print(groups)