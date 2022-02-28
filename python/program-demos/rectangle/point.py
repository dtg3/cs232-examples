import math

class Point:
    """2D Point class

    Support for sorting data necessary to 
    perform basic calculations on 2D points

    Attributes:
        x (float): the x coordinate for the point
        y (float): the y coordiante for the point
    """


    def __init__(self, x_pos, y_pos):
        """Initialize the point with an x and y position"""
        self.x = x_pos
        self.y = y_pos


    def __str__(self):
        """Override the provided __str__ function for printing
        
        This function will be called anytime the 
        print() function is used with the Point class
        to render the content in a human readable format.

        Return:
            string: return a string formatted as (x, y)
        """
        return f"({self.x}, {self.y})"


    def distance(self, destination_point):
        """Calcuate the distance to another point
        Args:
            destination_point (Point): second point for 
                distance calclation
        Return:
            float: distance to destination_point
        """
        return math.sqrt(
            (destination_point.x - self.x)**2 +
            (destination_point.y - self.y)**2)


    def midpoint(self, destination_point):
        """Calcuate the mid point to another point
        Args:
            destination_point (Point): second point for 
                midpoint calclation
        Return:
            Point: the calculated midpoint 
        """
        mid_x = (destination_point.x + self.x) / 2
        mid_y = (destination_point.y + self.y) / 2
        return Point(mid_x, mid_y)
