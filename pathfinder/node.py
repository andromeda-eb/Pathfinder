WHITE = (255, 255, 255)	# default
GREEN = (0, 255, 0)		# start,end, path
BLUE = (0, 0, 255)		# open
BLACK = (5, 5, 5)		# barrier
RED = (255, 0, 0)		# closed


class Node():
    def __init__(self, row, column, width, row_size, pygame):
        self.row = row
        self.column = column
        self.x = row * width
        self.y = column * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.height = width
        self.row_size = row_size
        self.pygame = pygame

    def get_position(self):
        return ( self.row, self.column )

    def is_barrier(self):
        return self.color == BLACK

    def reset(self):
        self.color = WHITE

    def set_start(self):
        self.color = GREEN

    def set_end(self):
        self.color = GREEN

    def set_barrier(self):
        self.color = BLACK

    def set_open(self):
        self.color = BLUE

    def set_shortest_path(self):
        self.color = GREEN

    def set_closed(self):
        self.color = RED

    def draw(self, window):
        self.pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def set_neighbours(self, grid):
        neighbour_coords = [
            # cost and coordinates
            ( 10, (self.row, self.column - 1) ),		# north
            ( 14, (self.row + 1, self.column - 1) ),    # north east
            ( 10, (self.row + 1, self.column) ),		# east
            ( 14, (self.row + 1, self.column + 1) ),    # south east
            ( 10, (self.row, self.column + 1) ),	    # south
            ( 14, (self.row - 1, self.column + 1) ),    # south west
            ( 10, (self.row - 1, self.column) ),		# west
            ( 14, (self.row - 1, self.column - 1) )     # north west
        ]

        for n in neighbour_coords:
            # if within range and not a barrier
            if 0 <= n[1][0] < self.row_size and 0 <= n[1][1] < self.row_size and not grid[n[1][0]][n[1][1]].is_barrier():
                self.neighbours.append(n)

    def get_neighbours(self):
        return self.neighbours
