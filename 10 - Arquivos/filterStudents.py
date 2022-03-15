def filterStudents(record, n):
    for line in record.readlines():
        line = line.split()
        if len(line) < 2:
            continue
        student = line[0]
        grades = line[1:]
        if len(grades) >= n:
            print(student)


def main():
    print("This program reads a record of the students' grades and prints only the names of those that've been evaluated at least a given amount of times.")

    record = open(input("Type the filename of the record: "), "r")
    filterStudents(record, int(input("Type the minimum amount of evaluations: ")))
    record.close()


main()
