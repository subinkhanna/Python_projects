class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Area of rectangle is {self.width * self.height}"

    @property
    def width(self):
        return f"{self._width:.2f} cms"
    
    @property
    def height(self):
        return f"{self._height:.2f} cms"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width has to be GT 0")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height has to be GT 0")

    @width.deleter
    def width(self):
        del self._width
        print(f"Attribute width has been deleted")

rectangle = Rectangle(3,3)

print(rectangle.width, rectangle.height)

del rectangle.width