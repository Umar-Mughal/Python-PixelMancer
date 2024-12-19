import sys
import os
from PIL import Image

# grab first and second argument from terminal: python3 jpg_to_png_converter.py images/ new/
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check is new/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through /images folder, convert images to png, save them to /new folder
for file_name in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file_name}')
    clean_name = os.path.splitext(file_name)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print(f'Current image:', file_name)