import qrcode

codeText = 'http://cdn.thu.edu.tw/'
img = qrcode.make(codeText)
print('檔案格式', type(img))
img.save('thu.jpg')
