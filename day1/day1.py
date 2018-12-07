from functools import reduce

def readFile(filename):
    with open(filename) as f:
        return f.readlines()

def stripContent(content):
    return [int(x.strip()) for x in content]

if __name__ == '__main__':
    content = readFile("input.txt")
    inputs = stripContent(content)
    print(reduce(lambda a,b: a+b, inputs,0))
