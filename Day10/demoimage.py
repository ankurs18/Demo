#pillow

from PIL import Image

img = Image.open('sample.jpeg')
print(img.size)
print(img.format)

img90 = img.rotate(90).save('img90.jpeg')
img45 = img.rotate(45).save('img45.jpeg')

cropImg = img.crop((10,10,200,200))
cropImg.save('nimage.jpeg')