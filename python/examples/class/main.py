# Local Modules
from point import Point
from rectangle import Rectangle


def main():
    # Assemble the vetices of the rectangle
    # using the Point class
    top_left = Point(1, 2)
    top_right = Point(5, 2)
    bottom_right = Point(5, -1)
    bottom_left = Point(1, -1)
    
    # Pass all the points to the rectangle
    # class
    shape = Rectangle(top_left, top_right,
                      bottom_right,
                      bottom_left)
    
    # Print out some of the calculated information
    print(f"Rect Perimeter: {shape.perimeter()}")
    print(f"Rect Area: {shape.area()}")

    # Use the Points that make up the vertices of the
    # rectangle to compute a point at the center of the
    # rectangle.
    print(f"Rect Center: {top_left.midpoint(bottom_right)}")


if __name__ == "__main__":
    main()
