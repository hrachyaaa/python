import math  

class Shape: 
    pass 

class TwoDimensional(Shape): 
    def area(self): 
        pass 

class ThreeDimensional(Shape): 
    def area(self): 
        pass 

    def volume(self): 
        pass 

class Square(TwoDimensional): 
    def __init__(self, side_length): 
        self.__side_length = side_length 

    def area(self): 
        return self.__side_length ** 2 

class Triangle(TwoDimensional): 
    def __init__(self,side_a, side_b, side_c ): 
        self.__side_a = side_a 
        self.__side_b = side_b 
        self.__side_c = side_c 

    def area(self): 
        p = (self.__side_a + self.__side_b + self.__side_c) / 2 
        return math.sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c)) 

class Cube(ThreeDimensional): 
    def __init__(self, side_length): 
        self.__side_length = side_length 

    def area(self): 
        return 6 * pow(self.__side_length,2) 

    def volume(self): 
        return self.__side_length ** 3 

class Cone(ThreeDimensional): 
    def __init__(self, radius, height): 
        self.__radius = radius 
        self.__height = height 

    def  area(self): 
      return math.pi * self.__radius * (self.__radius + math.sqrt(self.__height ** 2 + self.__radius ** 2))

    def volume(self): 
        return (1/3) * math.pi * (self.__radius ** 2) * self.__height 


mySquare = Square(7) 
myTriangle = Triangle(6,8,10) 
myCube = Cube(10) 
myCone = Cone(4, 10) 

print("Area of square: ", mySquare.area()) 
print("Area of triangle: ", myTriangle.area()) 

print("Area of Cube: ", myCube.area()) 
print("Volume of Cube: ", myCube.volume()) 

print("Area of Cone: ", myCone.area()) 
print("Volume of Cone: ", myCone.volume())
