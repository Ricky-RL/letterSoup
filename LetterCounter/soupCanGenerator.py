from letterCounter import generateAlphabetKeys
from string import ascii_lowercase as alc
import numpy as np


canOfSoupSize = 180
#generaets a random can of soup and returns it
def generateSoupCan():
    return [*map(lambda x: np.round(x * canOfSoupSize), np.random.dirichlet(np.ones(26),size=1).tolist()[0])]


#produces an average can of soup averaging n > 0 number of times
def averageAlphabetSoup(n):
    dict = generateAlphabetKeys()
    can = [0] * 26
    for i in range(n):
        can = [x + y for x, y in zip(can, generateSoupCan())]

    count = 0
    for c in alc:
        dict[c] = np.round(can[count] / n)
        count += 1

    return dict




print(averageAlphabetSoup(5))
print(sum(averageAlphabetSoup(5).values()))




