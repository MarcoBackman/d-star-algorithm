

class TextParser:

    # creates a grid initialized with a empty list
    def __init__(self):
        self.grid = []

    # takes in a file returns a 2d list of characters (doesnt include border)
    def parse_file(self, input_file):
        with open(input_file, ) as in_file:
            for line in in_file:
                row = [line[i] for i in range(0, len(line.strip()), 2) if line[i] != 'W']
                if row:
                    self.grid.append(row)
            return self.grid
