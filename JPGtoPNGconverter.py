import sys
import os
from PIL import Image

# Hardcoded paths based on your setup
source_folder = 'Pokedex'
destination_folder = 'new'

# Create the 'new' folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in Pokedex
for filename in os.listdir(source_folder):
    full_path = os.path.join(source_folder, filename)

    # Skip folders
    if os.path.isdir(full_path):
        continue

    # Only process JPG/JPEG files
    if not filename.lower().endswith(('.jpg', '.jpeg')):
        continue

    try:
        clean_name = os.path.splitext(filename)[0]
        img = Image.open(full_path)
        output_path = os.path.join(destination_folder, f'{clean_name}.png')
        img.save(output_path, 'png')
        print(f'Converted: {filename} → {clean_name}.png')
    except Exception as e:
        print(f'Error converting {filename}: {e}')

print('✅ All images converted!')
