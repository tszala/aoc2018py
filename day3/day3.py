import sys
import os
from itertools import product
from itertools import groupby
from itertools import chain
import re
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\common'))

from fileutils import FileReader

#13 @ 249,936: 13x11
pattern=re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

#claim (number, xoffset, yoffset, x, y):

def parse_claim(text):
    m=pattern.match(text)
    return (int(m.groups()[0]), int(m.groups()[1]), int(m.groups()[2]), int(m.groups()[3]), int(m.groups()[4]))

# claim to tuples of requested inches
def claimed_squares(claim):
    xoffset=claim[1]
    yoffset=claim[2]
    x=claim[3]
    y=claim[4]
    return [(i,j) for i in range(xoffset, xoffset+x) for j in range(yoffset, yoffset+y)]

def part_one(claims):
    print("Part One")
    coordinates_lists = [claimed_squares(claim) for claim in claims]
    coordinates = sorted([y for x in coordinates_lists for y in x])
    grouped = {k:len(list(group)) for k, group in groupby(coordinates) if len(list(group)) > 1}
    print("Number of inches with more than 1 claim: %i" % len(grouped))

def p2(d):
    rect = np.zeros((1000, 1000))
    for claim in d:
        iden, leftoff, topoff, w, h = claim
        rect[leftoff:leftoff + w, topoff:topoff+h] += 1
    for claim in d:
        iden, leftoff, topoff, w, h = claim
        if np.all(rect[leftoff:leftoff + w, topoff:topoff+h] == 1):
            return iden

def intersecting(a, b):
    return (not (a[1] <= b[0] or a[0] >= b[1]))

def intersecting2(a, b):
    return (((a[0] <= b[0] and a[1] > b[0]) or (a[0] < b[1] and a[1] >= b[1]))
        or ((b[0] <= a[0] and b[1] > a[0]) or (b[0] < a[1] and b[1] >= a[1])))

def check_intersections(claims, current_claim):
    bx=current_claim[1]
    by=current_claim[1] + current_claim[3]
    dx=current_claim[2]
    dy=current_claim[2] + current_claim[4]
    for claim in claims:
        if claim[0]!=current_claim[0]:
            ax=claim[1]
            ay=claim[1] + claim[3]
            cx=claim[2]
            cy=claim[2] + claim[4]
            if (intersecting((ax,ay),(bx,by)) and intersecting((cx,cy),(dx,dy))):
                return True

    return False

def part_two(claims):
    print("Part Two")
    for claim in claims:
        i=check_intersections(claims, claim)
        if not i:
            print("Found not intersecting claim %i " % claim[0])
            print(claim)
            return

def full_group_by(l, key=lambda x: x):
    d = defaultdict(list)
    for item in l:
        d[key(item)].append(item)
    return d.items()

if __name__ == '__main__':
    print("Advent of Code day 3")
    f = FileReader()
    input = f.readFile("input.txt")
    #input= ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2']
    print("Read %(number)i lines as input" % {'number':len(input)})
    claims = [parse_claim(line) for line in input]
    print("Read %(number)i of different claims" % {'number':len(claims)})
    part_one(claims)
    part_two(claims)
    print("Part two with numpy")
    print(p2(claims))
