def reverse(list, length):
    if length == 1:
        return [list[0]]
    return [list[length - 1]] + reverse(list, length - 1)


def main():
    print("This program prints a reversed list of values in reverse order.")

    list=input("Type in a comma separated list of values: ").split(',')
    for i in list:
        i=i.lstrip(' ')
    print(reverse(list, len(list)))


main()
