class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return (self.x, self.y)

    def reflect_x(self):
        self.y = -self.y


def main():
    print("This program calculates the coordinates of the reflection of a point along the x axis.")

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
    p = Point(coordinates[0], coordinates[1])
    print("The reflection of", p.coordinates(), end=' ')
    p.reflect_x()
    print("is", p.coordinates())


main()
