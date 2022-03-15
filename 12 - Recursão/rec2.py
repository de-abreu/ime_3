def listSum(integers):
    if len(integers) == 1:
        return integers[0]
    return integers[0] + listSum(integers[1:])


def main():
    strings = input().split()
    integers = []
   
    for i in strings:
        integers.append(int(i))
    print(listSum(integers))


main()
