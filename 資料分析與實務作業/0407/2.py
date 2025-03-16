from PIL import Image
from PIL import ImageColor

newImage = Image.open('out.jpg')
for x in range(50, 251):
    for y in range(40, 91):
        newImage.putpixel((x, y), ImageColor.getcolor('Blue', 'RGB'))
for x in range(50, 251):
    for y in range(91, 141):
        newImage.putpixel((x, y), ImageColor.getcolor('Red', 'RGB'))
newImage.save('out1.jpg')
