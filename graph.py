class Vertex:
    def __init__(self, v_type):
        self.v_type = v_type
        self.adjacent = []  # ordered by up left down right
        self.visited = False
        self.is_obstacle = (v_type == 'X')

    # adds edge from self to vertice
    def add_adj(self, vertex):
        self.adjacent.append(vertex)
        if len(self.adjacent) == 4:
            self.reorder_adj()

    # gets adjacent from index
    def get_adj(self, index):
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
            row[0].add_adj(None)  # adds left at start of row
            for x in range(1, len(grid[0])):
                row.append(Vertex(grid[y][x]))
                self.find_r_or_g(grid[y][x], row[x])
                self.connect_vertices(prev_row[x], row[x])  # connects current vertex with vertex above it
                self.connect_vertices(row[x-1], row[x])  # connects current vertex with previous vertex on left
            row[-1].add_adj(None)  # adds right to end of list
            prev_row = row[:]
            row.clear()

        # adds none to 'down' and reorders adjacent list
        for x in range(len(prev_row)):
            prev_row[x].add_adj(None)

    def connect_vertices(self, vertex1, vertex2):
        # vertex1 on left/above vertice2 on right/below
        if vertex1 is not None:
            vertex1.add_adj(vertex2)
        if vertex2 is not None:
            vertex2.add_adj(vertex1)

    def find_r_or_g(self, c, vertex):
        if c == 'G':
            self.start = vertex
        elif c == 'R':
            self.goal = vertex

    def __str__(self):
        msg = ""
        y_vertex = self.root
        while y_vertex is not None:
            x_vertex = y_vertex
            while x_vertex is not None:
                msg += f"{x_vertex.v_type}"
                x_vertex = x_vertex.get_adj(3)
            msg += '\n'
            y_vertex = y_vertex.get_adj(2)
        return msg
