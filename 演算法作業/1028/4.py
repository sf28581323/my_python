class Polynomial():
    def __init__(self,A,B):
        self.A = A
        self.B = B

    def add (self):
        b=[]
        for i in range(len(self.A)):
            b.append(int(self.A[i])+int(self.B[i]))
        return b[1:]
    
    def sub(self):
        b=[]
        for i in range(len(self.A)):
            b.append(int(self.A[i])-int(self.B[i]))
        return b[1:]
    
    def mul(self):
        b = [0 for i in range(self.A[0]+self.B[0]+1)]
        self.A.reverse()
        self.B.reverse()

        for i in range(len(self.A)-1):
            for j in range(len(self.B)-1):
                X = self.A[i]*self.B[j]
                Y = i+j
                b[Y] = b[Y]+X
        b.append(self.A[-1]+self.B[-1])
        b.reverse()
        return(b)
            
A = [4,3,7,6,0,2]
B = [4,1,5,2,0,9]
C = Polynomial(A,B)
print(C.add())
print(C.sub())
print(C.mul())
