class Vertex:
    def __init__(self, v_type):
        self.v_type = v_type
        self.adjacent = []  # ordered by up left right down
        self.visited = False
        self.is_obstacle = (v_type == 'X')

    # adds edge from self to vertice
    def add_edge(self, vertice):
        self.adjacent.append(vertice)

    # gets adjacent from index
    def get_adjacent(self, index):
        return self.adjacent[index]

    # reorders after all adj are added, changes adj u l r d to u l d r (swap d and r)
    def reorder_adj(self):
        self.adjacent[2], self.adjacent[3] = self.adjacent[3], self.adjacent[2]

class Graph:
    def __init__(self):
        self.start = None
        self.goal = None
        self.root = None

    def grid_to_graph(self, grid):
        # creates a prev row that starts as none and row that is later appended
        prev_row = [None] * len(grid[0])
        row = []

        # connects the current row then connects current row to previous row
        for y in range(len(grid)):
            row.append(Vertex(grid[y][0]))
            if y == 0:
                self.root = row[0]
            self.find_r_or_g(grid[y][0], row[0])
            self.connect_vertices(prev_row[0], row[0])  # adds row up and prevrow down
            if prev_row[0] is not None:
                prev_row[0].reorder_adj()
            row[0].add_edge(None)  # adds left at start of row
            for x in range(1, len(grid[0])):
                row.append(Vertex(grid[y][x]))
                self.find_r_or_g(grid[y][x], row[x])
                self.connect_vertices(prev_row[x], row[x])  # connects current vertex with vertex above it
                # reorder previous row (does not include initial none row)
                if y > 0:
                    prev_row[x].reorder_adj()
                self.connect_vertices(row[x-1], row[x])  # connects current vertex with previous vertex on left
            row[-1].add_edge(None)  # adds right to end of list
            prev_row = row[:]
            row.clear()

        # adds none to 'down' and reorders adjacent list
        for x in range(len(prev_row)):
            prev_row[x].add_edge(None)
            prev_row[x].reorder_adj()


    def connect_vertices(self, vertice1, vertice2):
        # vertice1 on left/above vertice2 on right/below
        if vertice1 is not None:
            vertice1.add_edge(vertice2)
        if vertice2 is not None:
            vertice2.add_edge(vertice1)

    def find_r_or_g(self, c, vertice):
        if c == 'G':
            self.start = vertice
        elif c == 'R':
            self.goal = vertice

    def __str__(self):
        msg = "Grid\n"
        y_vertice = self.root
        while y_vertice is not None:
            x_vertice = y_vertice
            while x_vertice is not None:
                msg += f"{x_vertice.v_type}"
                x_vertice = x_vertice.get_adjacent(3)
            msg += '\n'
            y_vertice = y_vertice.get_adjacent(2)
        return msg
