import math
class shape:
    def calc(self):
        pass
    def printing(self,area):
        print("The area is: ",area,"sq. meters")
class circle(shape):
    def __init__(self):
        self.r=float(input("Enter radius: "))
    def calc(self):
        area=math.pi*self.r*self.r
        return area
class rectangle(shape):
    def __init__(self):
        self.l=float(input("Enter length and breadth: "))
        self.b=float(input())
    def calc(self):
        area=self.l*self.b
        return area
class triangle(shape):
    def __init__(self):
        self.a = float(input("Enter 3 sides: "))
        self.b = float(input())
        self.c = float(input())
    def calc(self):
        s=(self.a+self.b+self.c)/2
        area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return area
ob=circle()
area=ob.calc()
ob.printing(area)
ob=rectangle()
area=ob.calc()
ob.printing(area)
ob=triangle()
area=ob.calc()
ob.printing(area)

