from grid import Grid
from menu import Menu
from algorithms import *


WHITE = (255, 255, 255)
BLACK = (5, 5, 5)

class Pathfinder():
    def __init__(self, window, width, grid_size, menu_size, pygame):
        self.pygame = pygame
        self.window = window
        self.width = width
        self.height = width
        self.grid_size = grid_size
        self.gap = self.width // self.grid_size
        self.menu_size = menu_size
        self.font = self.pygame.font.SysFont("Arial", 15)
        self.commands = ["BFS", "DFS", "Djikstra", "A*", "Reset"]

    def get_clicked_position(self, position):
        y, x = position

        row = y // self.gap
        column = x // self.gap

        return row, column

    def draw(self, grid, menu):
        self.window.fill(WHITE)
        grid.draw_grid()
        menu.draw_menu()
        self.pygame.display.update()

    def run_algorithm(self, window, draw, grid_obj, command):
        start = grid_obj.get_start()
        end = grid_obj.get_end()

        if not start and not end: return

        grid = grid_obj.get_grid()
        start_position = start.get_position()
        end_position = end.get_position()

        if command == "BFS":
            breadth_first(window, draw, grid, start_position, end_position)

        elif command == "DFS":
            depth_first(window, draw, grid, start_position, end_position)

        elif command == "Djikstra":
            djikstra(window, draw, grid, start_position, end_position)

        elif command == "A*":
            a_star(window, draw, grid, start_position, end_position)

    def reset_grid(self, grid):
        grid.init_grid()
        grid.start = None
        grid.end = None

    def start(self):
        run = True
        grid = Grid(self.window, self.grid_size, self.width, self.gap, self.pygame)
        menu = Menu(self.window, self.width, self.font, self.menu_size, self.commands, self.pygame)

        while run:
            self.draw(grid, menu)

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    run = False

                elif self.pygame.mouse.get_pressed()[0] or self.pygame.mouse.get_pressed()[2]:
                    position = self.pygame.mouse.get_pos()
                    row, column = self.get_clicked_position(position)

                    if row < self.grid_size and column < self.grid_size and self.pygame.mouse.get_pressed()[0]: # left click
                        grid.add_node(row, column)

                    elif row < self.grid_size and column < self.grid_size and self.pygame.mouse.get_pressed()[2]: # right click
                        grid.remove_node(row, column)

                    else:
                        command = menu.select_command(self.pygame.mouse.get_pos()[0])

                        if command != "Reset":
                            self.run_algorithm(self.window, lambda: self.draw(grid, menu), grid, command)

                        else:
                            self.reset_grid(grid)



        self.pygame.quit()
