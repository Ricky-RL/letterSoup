import pathlib
# Counts the amount of letters in a given text file and returns its dictionary
def countLetters (fileName, fileType):
    path = str(pathlib.Path().resolve()) + "\\textFiles"
    if fileType == "book":
        path += "\\books"
    elif fileType == "movie":
        path += "\\movies"

    letters = generateAlphabetKeys()
    with open(path + "\\" + fileName) as file:
        for line in file:
            for char in line:
                if char in letters.keys():
                    letters[char] += 1

    return letters


# Generates a dictionary for the alphabet, initializng all values to 0, returns dictionary
def generateAlphabetKeys():
    dict = {}
    str = "abcdefghijklmnopqrstuvwxyz"
    for c in str:
        dict[c] = 0
    return dict