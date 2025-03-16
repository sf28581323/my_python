from PIL import Image

pict = Image.open('dog.jpg')
newPict = Image.new('RGB',(800+100, 400+100),'Yellow')
for x in range(0, 8):
    for y in range(0, 4):
        newPict.paste(pict, (50+100*x, 50+100*y))
newPict.save('5xxx.jpg')
