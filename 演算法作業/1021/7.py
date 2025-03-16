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

s=Shape()
t=Tri('三角形',3,4,5)
print(s.name)
print(t.name,'周長為'+str(t.length()))
