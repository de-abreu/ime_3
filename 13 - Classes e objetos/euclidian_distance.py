class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return (self.x, self.y)

    def distance(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5


def main():
    print("This program calculates the euclidian distance between two points")

    data = input(
        "Type in, separated by spaces, the x and y coordinates of the two points, respectively: ").split()
    count = 0
    coordinates = []
    for i in data:
        try:
            coordinate = float(i)
        except ValueError:
            print("Warning: \"" + i + "\" is not a number, ignored.")
        else:
            coordinates.append(coordinate)
            count += 1
    if count < 4:
        if 4 - count == 1:
            print("Error: missing a coordinate.")
        else:
            print("Error: missing", 4 - count, "coordinates.")
        return
    p = Point(coordinates[0], coordinates[1])
    q = Point(coordinates[2], coordinates[3])
    print("The distance between", p.coordinates(),
          "and", q.coordinates(), "is", p.distance(q))


main()
