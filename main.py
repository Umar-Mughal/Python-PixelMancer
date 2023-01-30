from PIL import Image

img = Image.open('./images/4.3 pikachu.jpg')
new_image = img.convert('L')  # grey image
box = (100, 100, 400, 400)
cropped_image = new_image.crop(box)
cropped_image.save('new_image.png', 'png')
print(f'Image size is: {cropped_image.size}')
