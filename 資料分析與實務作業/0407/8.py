from PIL import Image, ImageDraw

newImage = Image.new('RGB', (300, 300), 'Yellow')
drawObj = ImageDraw.Draw(newImage)

for x in range(100, 200, 3):
    for y in range(100, 200, 3):
        drawObj.point([x, y], fill = 'Green')

drawObj.line([(0, 0), (299, 0), (299, 299), (0, 299), (0, 0)], fill = 'Black')

for x in range(150, 300, 10):
    drawObj.line([(x, 0), (300, x-150)], fill = 'Blue')

for x in range(150, 0, -10):
    drawObj.line([(x, 0), (0, 150-x)], fill = 'Blue')

for y in range(150, 300, 10):
    drawObj.line([(0, y), (y-150, 300)], fill = 'Blue')

for y in range(300, 150, -10):
    drawObj.line([(300, 450-y), (y, 300)], fill = 'Blue')

newImage.save('8xxx.jpg')
