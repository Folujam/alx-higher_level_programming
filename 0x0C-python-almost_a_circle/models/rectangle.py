#!/usr/bin/python3
"""
First Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    child(Rectangle) inherits for parent(Base)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing parameters(attributes) listed above
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """private to public"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width attr"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """private to public"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height attr"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """private to public"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """private to public"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """displays elem in attr"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns print of str"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.widht, self.height)

    def update(self, *args, **kwargs):
        """updates elem in attr"""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
