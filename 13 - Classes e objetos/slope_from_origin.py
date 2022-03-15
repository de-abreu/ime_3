class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return (self.x, self.y)

    def slope_from_origin(self):
        return 0 if self.x == 0 else self.y / self.x


def main():
    print("This program calculates the slope between a given point and the origin of the system ofcoordinates.")

    data = input(
        "Type in, separated by spaces, the x and y coordinates of a point, respectively: ").split()
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
    if count < 2:
        if count == 1:
            print("Error: missing a coordinate.")
        else:
            print("Error: no coordinates given.")
        return
    print(Point(coordinates[0], coordinates[1]).slope_from_origin())


main()
