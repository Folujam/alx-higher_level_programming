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
