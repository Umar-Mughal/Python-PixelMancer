from PIL import Image

img = Image.open('./images/4.3 pikachu.jpg')
img.thumbnail((400, 150))
img.save('new_image.png', 'png')
print(img.size)
