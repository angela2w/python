class Shape:
    def __init__(self,lenght,height,width,base):
        self.lenght=lenght
        self.height=height
        self.width=width
        self.base=base

    def area(self):
        print()

class Triangle(Shape):
    def __init__(self,base,width):
        super().__init__(base,width)


