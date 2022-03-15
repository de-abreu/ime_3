def analysis(string):
    if (string == ""):
        print("Seu texto encontra-se vazio.")
        return

    words = 0
    words_with_e = 0
    previous_char = " "
    found_e = False

    for char in string:
        if (char != " " and previous_char == " ")\
        or (char == "-" and previous_char != " "):
            words += 1
            if found_e:
                words_with_e += 1
                found_e = False
        if char == "e":
            found_e = True
        previous_char = char
    if found_e:
        words_with_e += 1

    print("Seu texto contém", words, "palavras, das quais", words_with_e,
          "(", words_with_e / words * 100, "%) contém um \'e\'.")


print("Este programa recebe uma sequência de texto e apresenta uma análise deste.")

analysis(input("Digite uma sequência de texto: "))
