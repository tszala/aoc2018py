import sys
import os
from itertools import product


sys.path.append(os.path.join(os.path.dirname(__file__), '..\\common'))

from fileutils import FileReader

def wordToOccurences(word):
    return list(set([(f, word.count(f)) for f in word]))

def wordWithLetterOccuring(word, times):
    occurences=[tupple[1] for tupple in wordToOccurences(word)]
    return times in occurences

def numberOfDifferences(word1, word2):
    return sum([1 for i in range(0, len(word1) - 1) if word1[i] != word2[i]])    

def commonPart(word1, word2):
    return ''.join([word1[i] for i in range(0, len(word1) - 1) if word1[i] == word2[i]])

def partOne(input):
    elementsWithTwoLetters = [word for word in input if wordWithLetterOccuring(word, 2)]
    elementsWithThreeLetters = [word for word in input if wordWithLetterOccuring(word, 3)]
    print("Elements with 2 letters: %i, elements with three letters: %i" % (len(elementsWithTwoLetters), len(elementsWithThreeLetters)))
    print("Multiplying the above by itself gives following result: %i" % (len(elementsWithTwoLetters) * len(elementsWithThreeLetters)))

def partTwo(input):
    combinations = list(product(input,input))
    wordsWithSingleDifference = [tupple for tupple in combinations if numberOfDifferences(tupple[0], tupple[1]) == 1]
    print("Count of words with single letter difference %i" % len(wordsWithSingleDifference))
    for result in wordsWithSingleDifference:
        print("%s, %s" % (result[0], result[1]))
    common=commonPart(wordsWithSingleDifference[0][0], wordsWithSingleDifference[0][1])
    print("Common part is %s" % common)

if __name__ == '__main__':
    print("Advent of Code day 2")
    f = FileReader()
    content = f.readFile("input.txt")
    print("Read %(number)i lines" % {'number' : len(content)})
    partOne(content)
    partTwo(content)
