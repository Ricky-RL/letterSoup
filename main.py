from FileLetterCounter.letterCounter import *

dict = countLetters("bible", "book")
print(dict)
print(max(dict, key=dict.get), ":", max(dict.values()))
