class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def coordinates(self):
        return (self.x, self.y)

    def distance(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5

    def on(self, rect):
        if self.x >= rect.corner.x and \
           self.x <= rect.corner.x + rect.length and \
           self.x >= rect.corner.x and \
           self.x <= rect.corner.x + rect.length:
           return True
        return False


class Rectangle:
    """ Performs calculations on rectangles."""

    def __init__(self, point, length, height):
        self.corner = point
        self.length = float(length)
        self.height = float(height)

    def area(self):
        return self.length * self.height

    def perimeter(self):
        return 2 * (self.length + self.height)

    def transpose(self):
        tmp = self.length
        self.length = self.height
        self.height = tmp

    def collides(self, rect):
        if self.corner.x < rect.corner.x + rect.length and \
                self.corner.x + self.length > rect.corner.x and \
                self.corner.y < rect.corner.y + rect.height and \
                self.corner.y + self.height > rect.corner.y:
            return True
        return False


def main():
    print("This program perform calculations on rectangles. Let us first decribe a rectangle:")

    rect1 = Rectangle(
            Point(input("Give the x coordinate of bottom left corner: "),
                  input("Give the y coordinate of bottom left corner: ")),
            input("Give the rectangle's length: "),
            input("Give the rectangle's height: "))

    print("The area of this rectangle is", rect1.area(),
          "and its perimeter is", rect1.perimeter())
    print("Now we'll transpose such rectangle.")
    rect1.transpose()
    print("This rectangle's new length is", rect1.length,
          "and its height is", rect1.height)
    print("Test if a given point lies on the rectangle.")

    point = Point(input("Give the point's x coordinate: "),
                  input("And its y coordinate: "))
    if point.on(rect1):
        print("The point is on the rectangle.")
    else:
        print("The point is not on the rectangle.")
    print("Test if another rectangle collides with the first. Describe a new rectangle:")

    rect2 = Rectangle(
            Point(input("Give the x coordinate of bottom left corner: "),
                  input("Give the y coordinate of bottom left corner: ")),
            input("Give the rectangle's length: "),
            input("Give the rectangle's height: "))

    if rect1.collides(rect2):
        print("The rectangles are colliding.")
    else:
        print("The rectangles are not colliding.")


main()
