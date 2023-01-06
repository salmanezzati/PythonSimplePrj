


class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b 

    def __str__(self):
        return "Point X : {} , Point Y : {}".format(self.x,self.y)

    def __repr__(self):
        return "Point X : {} , Point Y : {}".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x 
        y = self.y + other.y 
        return "{} , {}".format(x,y)
        
    def __sub__(self,other):
        x = self.x - other.x 
        y = self.y - other.y 
        return Point(x,y)

myPoint_1 = Point(1,5)
myPoint_2 = Point(2,8)

print(myPoint_1 + myPoint_2)
print(myPoint_1 - myPoint_2)
