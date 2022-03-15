import string


def countWords(path, columnWidth):
    file = open(path, 'r')
    wordCount = dict()
    text = ""
    for c in file.read():
        if c in string.ascii_letters + string.whitespace + "-":
            text += c
    for word in text.lower().split():
        word = word.lstrip('-').rstrip('-')
        if word == '':
            continue
        wordCount[word] = wordCount.get(word, 0) + 1
        length = len(word)
        if length > columnWidth[0]:
            columnWidth[0] = length
    file.close()
    return wordCount


def selectFilename(path):
    beginning = path.rfind('/')
    if beginning == -1:
        beginning = 0
    else:
        beginning += 1
    end = path.rfind('.')
    if end < beginning:
        end = len(path)
    return path[beginning:end]


def main():
    print("This program counts words contained in a plain text file, and saves the results as \"wordCount_filename.dat\".")
    path = input("Type in a file's path: ")
    columnWidth = [0]
    wordCount = countWords(path, columnWidth)
    output = "word_count_" + selectFilename(path) + ".dat"
    output = open(output, 'w')
    output.write("Word" + ' ' * (columnWidth[0] - 4) + "\tfrequency\n")
    output.write("-" * columnWidth[0] + "\t" + "-" * columnWidth[0] + "\n")
    for word in sorted(wordCount):
        padding = columnWidth[0] - len(word)
        output.write(word + ' ' * padding + "\t" + str(wordCount[word]) + "\n")
    output.close()


main()
