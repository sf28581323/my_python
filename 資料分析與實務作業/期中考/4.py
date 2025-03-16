class CRect:
    def __init__(self,width,height,length):
        self.width=width
        self.height=height
        self.length=length
    def area(self):
        return self.width*self.length
    def volume(self):
        return self.width*self.length*self.height
    def show(self):
        area = self.width*self.length
        volume = self.width*self.length*self.height
        print('面積為',area)
        print('體積為',volume)

a = CRect(10,20,30)
b = CRect(40,20,60)
c = CRect(50,70,100)
a.show()
print('')
b.show()
print('')
c.show()
