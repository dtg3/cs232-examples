
class Rectangle:
    """Rectangle class

    Utilzes the point class to store the vertices
    of the rectangle. The rectangle must be
    constructed in the order top_left, top_right,
    bottom_right, and bottom_left (clockwise).

    Attributes:
        vertices (list): list of Point objects
        sides (list): length of sides starting with
            the top side and moving clockwise
    """

    def __init__(self, vertex1, vertex2, vertex3, vertex4):
        """Initialize the rectangle vertices and sides"""
        self.vertices = [vertex1, vertex2, vertex3, vertex4]
        self.sides = self._calculate_sides()


    def perimeter(self):
        """Use the side lengths to calculate the perimeter

        Return:
            number: perimeter of the rectangle
        """
        return sum(self.sides)

    
    def _calculate_sides(self):
        """Use the vertices to calculate side lengths

        Sides length calculated starting with the
        top side and moving clockwise. The "_" at the
        beginning of this function indicates that is 
        is intended to be private and should not be used
        by external code.

        Return:
            list: all sides stored start with the top and
                moving clockwise
        """
        sides = []
        sides.append(self.vertices[0].distance(self.vertices[1]))
        sides.append(self.vertices[1].distance(self.vertices[2]))
        sides.append(self.vertices[2].distance(self.vertices[3]))
        sides.append(self.vertices[3].distance(self.vertices[0]))
        return sides


    def area(self):
        """Use the side lengths to calculate area

        Return:
            number: area of the rectangle
        """
        return self.sides[0] * self.sides[1]
