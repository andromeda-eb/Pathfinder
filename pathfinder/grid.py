from node import Node

BLACK = (0, 0, 0)

class Grid():
    def __init__(self, window, size, width, gap, pygame):
        self.pygame = pygame
        self.window = window
        self.size = size
        self.gap = gap
        self.width = width
        self.grid = []
        self.init_grid()
        self.start = None
        self.end = None

    def init_grid(self):
        temp_grid = []

        for i in range(self.size):
            row = []

            for j in range(self.size):
                node = Node(i,j, self.gap, self.size, self.pygame)

                row.append(node)

            temp_grid.append(row)

        self.grid = temp_grid

    def update_node(self, row, column, node):
        self.grid[row][column] = node

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def draw_grid_lines(self):
        for i in range(self.size):
            self.pygame.draw.line(self.window, BLACK, (0, i * self.gap), (self.width, i * self.gap))

        for j in range(self.size):
            self.pygame.draw.line(self.window, BLACK, (j * self.gap, 0), (j * self.gap, self.width))

        self.pygame.draw.line(self.window, BLACK, (0, self.size * self.gap), (self.width, self.size * self.gap))

    def draw_grid_nodes(self):
        for row in self.grid:
            for node in row:
                node.draw(self.window)

    def draw_grid(self):
        self.draw_grid_nodes()
        self.draw_grid_lines()

    def get_grid(self):
        return self.grid

    def get_node(self, row, column):
        return self.grid[row][column]

    def add_node(self, row, column):
        node = self.grid[row][column]

        if not self.start and node != self.end:
            self.start = node

            self.start.set_start()

        elif not self.end and node != self.start:

            self.end = node

            self.end.set_end()

        elif node != self.start and node != self.end:

            node.set_barrier()

    def remove_node(self, row, column):
        node = self.grid[row][column]

        node.reset()

        if node == self.start:
            self.start = None
        elif node == self.end:
            self.end = None
