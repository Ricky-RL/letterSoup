from LetterCounter.letterCounter import *
from LetterCounter.soupCanGenerator import *
from string import ascii_lowercase as alc

dict = countLetters("bible", "book")

def getSoupCanAmount():

    cansOfSoup = 0
    enoughLetters = False
    currentLetters = generateSoupCan()

    while(not enoughLetters):
        i = 0
        for c in alc:
            if currentLetters[i] < dict[c]:
                break
            elif c == "z":
                enoughLetters = True
            i += 1

        currentLetters = [x + y for x, y in zip(currentLetters, generateSoupCan())]
        cansOfSoup += 1

    return cansOfSoup

print(getSoupCanAmount())





