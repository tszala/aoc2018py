import sys
import os
from itertools import product
import string

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\common'))

from fileutils import FileReader

units=string.ascii_lowercase

def react_polymer_once(polymer):
    reacted_polymer = ''
    previous = ''
    current = ''
    for i in range(len(polymer)):
        current = polymer[i]
        if previous == '':
            previous=current
            continue
        if reacting(previous, current):
            previous=''
        else:
            reacted_polymer += previous
            previous=current

    return reacted_polymer + previous

def reacting(a,b):
    return abs(ord(a)-ord(b)) == 32

def react_polymer(input):
    reduced = react_polymer_once(input)
    if len(reduced) < len(input):
        return react_polymer(reduced)
    else:
        return reduced

def react_polymer_iter(input):
    while True:
        current_length=len(input)
        input = react_polymer_once(input)
        if current_length == len(input):
            return input

def part_two(input):
    result = {}
    for letter in units:
        print("Removing unit %s" % letter)
        input_without_unit = input.replace(letter, '').replace(letter.upper(),'')
        result[letter] = react_polymer_iter(input_without_unit)

    best_item = sorted(result.items(), key=lambda x: len(x[1]))[0]
    print(len(best_item[1]))

if __name__ == '__main__':
    print("Advent of code Day 5")
    f = FileReader()
    input = f.readFile("input.txt")[0].strip()

    print("Read %i characters" % len(input))
    reacted_polymer=react_polymer_iter(input)
    print(reacted_polymer)
    print("Part one answer is %i" % len(reacted_polymer))
    part_two(input)
