import sys
import os
from functools import reduce

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\common'))

from fileutils import FileReader

def readFile(filename):
    with open(filename) as f:
        return f.readlines()

def stripContentAndConvertToInts(content):
    return [int(x.strip()) for x in content]

def calculateFrequenceWithFor(inputs, start):
    for input in inputs:
        start += input
    return start

def calculateFrequenceWithWhile(inputs, start):
    index = 0
    while index < len(inputs):
        start += inputs[index]
        index += 1
    return (start)

def findDoubledFrequency(inputs, frequency):
    found = False
    frequencies = {frequency}
    while not found:
        index = 0
        while index < len(inputs) and not found:
            frequency += inputs[index]
            index += 1
            if frequency in frequencies:
                found = True
            else:
                frequencies.add(frequency)

    return (frequency)


if __name__ == '__main__':
    f = FileReader()
    
    inputs = f.readInts("input.txt")

    print(reduce(lambda a,b: a+b, inputs,0))

    print(calculateFrequenceWithFor(inputs,0))

    print(calculateFrequenceWithWhile(inputs,0))

    print(findDoubledFrequency(inputs,0))
