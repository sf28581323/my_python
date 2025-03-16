from PIL import Image, ImageDraw, ImageFont


pict = Image.open('大頭照.jpg')
newPict1 = pict.resize((350, 500))
newPict2 = Image.new('RGB',(350+100, 500+250),'Yellow')
newPict2.paste(newPict1, (50, 50))

drawObj = ImageDraw.Draw(newPict2)

strCtext = '吳咸澄'
fontInfo = ImageFont.truetype('‪C:\Windows\Fonts\msjhbd.ttc', 48)
drawObj.text((155, 620), strCtext, fill = 'Blue', font = fontInfo)
newPict2.save('myfig2.jpg')
