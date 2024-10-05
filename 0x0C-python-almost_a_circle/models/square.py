#!/usr/bin/python3
"""
this is Square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this is the definition of Sqaure which inherits from
    Rectangle(Base)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing parameters(attributes) listed above
        """
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """returns str info for square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """return public gettr for size"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """this methods updates the class with the ffg:
        args: variable amount of arguments
        kwargs: variables amount of keyworded arguments

        if args and len(args) != 0:
            att = 0
            for arg in args:
                if att == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif att == 1:
                    self.size = arg
                elif att == 2:
                    self.x = arg
                elif att == 3:
                    self.y = arg
                att += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = key
                elif key == "x":
                    self.x = key
                elif key == "y":
                    self.y = key
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
