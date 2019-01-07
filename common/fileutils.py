class FileReader:
    def readFile(self, filename):
        with open(filename) as f:
            return f.readlines()

    def stripContentAndConvertToInts(self, content):
        return [int(x.strip()) for x in content]

    def readInts(self, filename):
        lines=self.readFile(filename)
        return self.stripContentAndConvertToInts(lines)
