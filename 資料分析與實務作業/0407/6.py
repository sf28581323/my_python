from PIL import Image

pict = Image.open('大頭照.jpg')
newPict = Image.new('RGB',(3306+100, 2836+100),'Yellow')
for x in range(0, 6):
    for y in range(0, 4):
        newPict.paste(pict, (50+551*x, 50+709*y))
newPict.save('myfig1.jpg')
