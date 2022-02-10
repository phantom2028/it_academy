class Rectangle:

    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width

    def get_square(self):
        global result_square
        result_square = self.__length * self.__width
        print(f"Square of rectangle is: {result_square}")

    def get_perimeter(self):
        global result_perimeter
        result_perimeter = (self.__length * 2) + (self.__width * 2)
        print(f"Perimeter of rectangle is: {result_perimeter}")

    @property
    def get_info_about_rec(self):
        print(f"We have rectange with length: {self.__length} and width: {self.__width}")
        print(f"Also, we have its square: {result_square}")
        print(f"And perimeter: {result_perimeter}")

rectangle = Rectangle(2, 5) 
rectangle.get_square()
rectangle.get_perimeter()
rectangle.get_info_about_rec
