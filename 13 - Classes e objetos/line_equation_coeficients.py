class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return (self.x, self.y)

    def angular_coeficient(self, point):
        delta_x = point.x - self.x
        delta_y = point.y - self.y
        return 0 if delta_x == 0 else delta_y / delta_x

    def linear_coeficient(self, point):
        return self.y - self.angular_coeficient(point) * self.x


def main():
    print("This program calculates the angular and linear coeficients, respectively, for a line drawn crossing two points.")

    data = input(
        "Type in, separated by spaces, the x and y coordinates of both points, respectively: ").split()
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
        if count == 3:
            print("Error: missing a coordinate.")
        else:
            print("Error: missing", 4 - count, "coordinates.")
        return
    p = Point(coordinates[0], coordinates[1])
    q = Point(coordinates[2], coordinates[3])
    print((p.angular_coeficient(q), p.linear_coeficient(q)))


main()
