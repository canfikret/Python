def find_word(word, matrix):
    for (i in matrix.height):
        for (j in matrix.length):
            if (matrix.length - j >= word.length):
                if (matrix.substringH(i, j, word.length) == word):
                    return (i,j, "H")

    for (i in matrix.length):
        for (j in matrix.height):
            if (matrix.height - j >= word.length):
                if (matrix.substringV(i, j, word.length) == word):
                    return (i,j, "V")

    return (-1, -1)
    
