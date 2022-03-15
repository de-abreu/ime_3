class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def coordinates(self):
        return (self.x, self.y)

    def distance(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5


class Circle:
    """ Coordinates for a circle of given center and radius """

    def __init__(self, p1, p2, p3):
        def repeated(p1, p2, p3):
            if p1 == p2 or p1 == p3 or p2 == p3:
                return True
            return False

        def colinear(p1, p2, p3):
            if (p2.x - p1.x) == 0 or (p3.x - p1.x) == 0:
                if (p1.x == p2.x and p1.x == p3.x) or \
                   (p1.y == p2.y and p1.y == p3.y):
                   return True
            elif (p2.y - p1.y) / (p2.x - p1.x) == (p3.y - p1.y) / (p3.x - p1.x):
                return True
            return False

        if repeated(p1, p2, p3) or colinear(p1, p2, p3):
            self.radius = None
            return

        d = p1.x * (p2.y - p3.y)
        d += p2.x * (p3.y - p1.y)
        d += p3.x * (p1.y - p2.y)
        d *= 2

        x = (p1.x ** 2 + p1.y ** 2) * (p2.y - p3.y)
        x += (p2.x ** 2 + p2.y ** 2) * (p3.y - p1.y)
        x += (p3.x ** 2 + p3.y ** 2) * (p1.y - p2.y)
        x /= d

        y = (p1.x ** 2 + p1.y ** 2) * (p3.x - p2.x)
        y += (p2.x ** 2 + p2.y ** 2) * (p1.x - p3.x)
        y += (p3.x ** 2 + p3.y ** 2) * (p2.x - p1.x)
        y /= d

        self.center = Point(x, y)
        self.radius = p1.distance(self.center)


def read_points():
    data = input(
        "Type in, separated by spaces, the x and y coordinates of the four points, respectively: ").split()

    coordinates = []
    for i in data:
        try:
            coordinate = float(i)
        except ValueError:
            print("Warning: \"" + i + "\" is not a number, ignored.")
        else:
            coordinates.append(coordinate)

    count = len(coordinates)
    if count < 8:
        if count == 7:
            print("Error: missing a coordinate.")
        else:
            print("Error: missing", 8 - count, "coordinates.")
        return None

    points = []
    for i in range(0, 8, 2):
        point = Point(coordinates[i], coordinates[i + 1])
        if point in points:
            print("Error: repeated point", point)
            return None
        points.append(point)
    return points


def main():
    print("This program calculates the center of a circle, given the location of four points on it.")

    points = read_points()
    if points is None:
        return

    circ = Circle(points[0], points[1], points[2])

    print("The points", end=' ')
    for p in points:
        print(p, end=", ")

    if circ.radius is None or points[0].distance(circ.center) != points[3].distance(circ.center):
        print("do not lie on the same circle.")
    else:
        print("lie on a circle of center",
              circ.center, "and radius", circ.radius)


main()
