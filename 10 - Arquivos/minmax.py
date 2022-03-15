def toint(input):
    output = []

    for i in input:
        output.append(int(i))
    return output


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


def minMaxScores(file, columnLength):
    record = open(file, "r")
    for line in record.readlines():
        line = line.split()
        if line == []:
            continue
        padding = " " * (columnLength - len(line[0]))
        grades = toint(line[1:])
        print("Student: " + line[0] + padding,
              "\tLowest score:", min(grades), "\tHighest score:", max(grades))
    record.close()


def main():
    print("This program reads a record of the students' grades and prints their average scores")

    file = input("Type in the filename of the record: ")
    minMaxScores(file, longestNameLength(file))


main()
