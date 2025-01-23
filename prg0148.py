class Point:
  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y
  def __str__(self):
    return "({0},{1})".format(self.x,self.y)
  
  def __add__(self,other):
      total = Point()  # 构造一个类 0 0
      # isinstance 判断是否是同一个类
      if isinstance(other, Point):
          total.x = self.x + other.x
          total.y = self.y + other.y
      else:
          total.x = self.x + float(other)
          total.y = self.y + float(other)
      return total
    
  def __radd__(self, point):
    total = Point()
    if isinstance(point, Point):
        total.x = self.x + point.x
        total.y = self.y + point.y
    else:
        total.x = self.x + float(point)
        total.y = self.y + float(point)
    return total
  def __sub__(self,other):
      total = Point()
      if isinstance(other, Point):
          total.x = self.x - other.x
          total.y = self.y - other.y
      else:
          total.x = self.x - float(other)
          total.y = self.y - float(other)
      return total
    
  def __rsub__(self, point):
      total = Point()
      if isinstance(point, Point):
          total.x = point.x - self.x
          total.y = point.y - self.y
      else:
          total.x = float(point) - self.x
          total.y = float(point) - self.y
      return total
    
  def __mul__(self, factor):
    total = Point()
    total.x = self.x * factor
    total.y = self.y * factor
    return total

  def __rmul__(self, factor):
      total = Point()
      total.x = self.x * factor
      total.y = self.y * factor
      return total
    
  def __eq__(self, value):
      return self.x == value.x and self.y == value.y
    
  def __ne__(self, value):
      return self.x != value.x or self.y != value.y
    
  def __lt__(self, value):
      return self.x < value.x and self.y < value.y  
    
  def __le__(self, value):
      return self.x <= value.x and self.y <= value.y  
    
  def __gt__(self, value):
      return self.x > value.x and self.y > value.y
    
  def __ge__(self, value):
      return self.x >= value.x and self.y >= value.y
    
  
    
if __name__ == "__main__":
  p1 = Point()
  print(p1.x,p1.y)
  print(p1+5)
  print(p1+Point(1,2))
  print(3-Point(3,4)-2)
  print(10*Point(1,2)*10)
  # 比较
  print(Point(1,2)==Point(1,2))# __eq__
  print(Point(1,2)!=Point(1,2))# __ne__
  print(Point(1,2)<Point(1,2)) # __lt__
  print(Point(1,2)<=Point(1,2)) # __le__
  print(Point(1,2)>Point(1,2))# __gt__
  print(Point(1,2)>=Point(1,2))# __ge__


  
