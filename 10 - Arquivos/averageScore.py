def toint(input):
    output = []

    for i in input:
        output.append(int(i))
    return output


def average(values):
    return round(sum(values) / len(values), 2)


def longestNameLength(file):
    record = open(file, "r")
    maxLength = 0
    for line in record.readlines():
        line = line.split()
        if line == []:
            continue
        nameLength = len(line[0])
        if nameLength > maxLength:
            maxLength = nameLength
    record.close()
    return maxLength


def averageScores(file, columnLength):
    record = open(file, "r")
    for line in record.readlines():
        line = line.split()
        if line == []:
            continue
        padding = " " * (columnLength - len(line[0]))
        print("Student: " + line[0] + padding,
              "\tAverage score:", average(toint(line[1:])))
    record.close()


def main():
    print("This program reads a record of the students' grades and prints their average scores")

    file = input("Type in the filename of the record: ")
    averageScores(file, longestNameLength(file))


main()
