def multiplicationTable(n):
    columnSize = 0
    biggestNumber = n * n

    while biggestNumber != 0:
        columnSize += 1
        biggestNumber //= 10

    for i in range(1, n + 1):
        print(str(i).ljust(columnSize), end="\t")
    print("")

    for i in range(n):
        print("-" * columnSize, end='\t')
    print("")

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end='\t')
        print("")


multiplicationTable(12)
