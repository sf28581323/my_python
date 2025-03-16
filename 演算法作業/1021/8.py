import math
class Shape:
    def __init__(self):
        self.name='形狀'
    def length(self):
        pass
class Tri(Shape):
    def __init__(self,name,length1,length2,length3):
        self.name=name
        self.length1=length1
        self.length2=length2
        self.length3=length3
    def length(self):
        return self.length1+self.length2+self.length3
class Rec(Shape):
    def __init__(self,name,length4,length5):
        self.name=name
        self.length4=length4
        self.length5=length5
    def length(self):
        return (self.length4+self.length5)*2
class Cir(Shape):
    def __init__(self,name,r):
        self.name=name
        self.r=r
    def length(self):
        return round(2*math.pi*self.r,1)
s=Shape()
t=Tri('三角形',3,4,5)
r=Rec('長方形',4,5)
c=Cir('圓形',5)
print(s.name)
print(t.name,'周長為'+t.length())
print(r.name,'周長為'+str(r.length()))
print(c.name,'周長為'+str(c.length()))
