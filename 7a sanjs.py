import math
class shape:
    def calc(self):
        pass
    def disp(self,area):
        print("area:",area)

class cir(shape):
    def __init__(self):
        self.r=float(input("enter radius"))

    def calc(self):
        self.area=math.pi*(self.r**2)
        return self.area

class rec(shape):
    def __init__(self):
        self.l=float(input("enter length and breadth"))
        self.b=float(input())

    def calc(self):
        area=self.l*self.b
        return area

class tri(shape):
    def __init__(self):
        self.a=float(input("enter 3 sides"))
        self.b=float(input())
        self.c=float(input())

    def calc(self):
        s=(self.a+self.b+self.c)/2
        area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return area

ob=cir()
area=ob.calc()
ob.disp(area)
ob=rec()
area=ob.calc()
ob.disp(area)
ob=tri()
area=ob.calc()
ob.disp(area)