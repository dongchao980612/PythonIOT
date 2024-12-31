class Rectangle:
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def perimeter(self ):
        return 2*(self.w+self.h)



if __name__ == '__main__':
    r = Rectangle(5,10)
    print(r.area(),r.perimeter())