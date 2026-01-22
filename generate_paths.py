#!/usr/bin/env python3
import os
import json

# Define the photo folders
folders = [
    'JP Morgan',
    'JP Morgan Asset Management',
    'JP Morgan Chase',
    'JP Morgan Chase Travel',
    'JP Morgan Private Bank',
    'JP Morgan Wealth Management'
]

# Image extensions to look for
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.PNG', '.JPG', '.JPEG')

photo_paths = {}

for folder in folders:
    folder_path = os.path.join('photos', folder)
    if os.path.exists(folder_path):
        photos = []
        for file in sorted(os.listdir(folder_path)):
            if file.endswith(image_extensions) and not file.lower().startswith('logo'):
                photos.append(f'photos/{folder}/{file}')
        photo_paths[folder] = photos
        print(f'{folder}: {len(photos)} photos')

# Generate the JavaScript object
js_code = 'const photoPaths = ' + json.dumps(photo_paths, indent=2) + ';'

# Read the HTML file
with open('index.html', 'r') as f:
    html_content = f.read()

# Replace the placeholder
html_content = html_content.replace('PHOTO_PATHS_PLACEHOLDER', json.dumps(photo_paths, indent=2))

# Write back the HTML file
with open('index.html', 'w') as f:
    f.write(html_content)

print('\nHTML file updated successfully!')
print(f'Total sections: {len(photo_paths)}')
print(f'Total photos: {sum(len(photos) for photos in photo_paths.values())}')
