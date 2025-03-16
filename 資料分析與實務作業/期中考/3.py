from PIL import Image, ImageDraw

newImage = Image.new('RGB', (300, 300), 'Red')
drawObj = ImageDraw.Draw(newImage)

for x in range(100, 200, 3):
    for y in range(100, 200, 3):
        drawObj.point([x, y], fill = 'Black')

drawObj.line([(0, 0), (299, 0), (299, 299), (0, 299), (0, 0)], fill = 'Blue')

for x in range(150, 300, 10):
    drawObj.line([(x, 0), (300, x-150)], fill = 'Black')

for x in range(150, 0, -10):
    drawObj.line([(x, 0), (0, 150-x)], fill = 'Black')

for y in range(150, 300, 10):
    drawObj.line([(0, y), (y-150, 300)], fill = 'Black')

for y in range(300, 150, -10):
    drawObj.line([(300, 450-y), (y, 300)], fill = 'Black')

newImage.save('3.jpg')
