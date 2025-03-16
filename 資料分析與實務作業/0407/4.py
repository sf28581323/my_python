from PIL import Image

pict = Image.open('大頭照.jpg')
newPict1 = pict.resize((350, 500))
newPict2 = Image.new('RGB',(350+100, 500+100),'Yellow')
newPict2.paste(newPict1, (50, 50))
newPict2.save('myfig.jpg')
