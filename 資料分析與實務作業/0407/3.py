from PIL import Image

pict = Image.open('大頭照.jpg')
width, height = pict.size

newPict1 = pict.resize((int(width*1.2), int(height)))
newPict1.save('3-w1.2.jpg')

newPict2 = pict.resize((int(width*1.5), int(height)))
newPict2.save('3-w1.5.jpg')

newPict3 = pict.resize((int(width*0.5), int(height)))
newPict3.save('3-w0.5.jpg')

newPict4 = pict.resize((int(width*0.8), int(height)))
newPict4.save('3-w0.8.jpg')

newPict5 = pict.resize((int(width), int(height*1.2)))
newPict5.save('3-h1.2.jpg')

newPict6 = pict.resize((int(width), int(height*1.5)))
newPict6.save('3-h1.5.jpg')

newPict7 = pict.resize((int(width), int(height*0.8)))
newPict7.save('3-h0.8.jpg')

newPict8 = pict.resize((int(width), int(height*0.5)))
newPict8.save('3-h0.5.jpg')
