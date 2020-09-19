WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Menu():
    def __init__(self, window, width, font, height, commands, pygame):
        self.pygame = pygame
        self.commands = commands
        self.command_count = len(self.commands)
        self.button_colors = [RED, BLUE]
        self.width = width
        self.button_width = self.width // self.command_count
        self.window = window
        self.font = font
        self.height = height

    def draw_text(self, button_name, button_position):
        x = button_position + ( (self.width // self.command_count)  // 2 ) - 20

        y = self.width + ( self.height // 2 )

        text = self.font.render(button_name, True, WHITE)

        self.window.blit(text, (x, y))

    def draw_button(self, position, color):
        self.pygame.draw.rect(self.window, BLACK, (position, self.width, self.button_width, self.height), 10) # button border

        self.pygame.draw.rect(self.window, color, (position, self.width, self.button_width, self.height))

    def draw_menu(self):
        for i in range(self.command_count):
            button_name = self.commands[i]

            button_position = (self.width // self.command_count) * i

            button_color = self.button_colors[0] if self.commands[i] == "Reset" else self.button_colors[1]

            self.draw_button(button_position, button_color)

            self.draw_text(button_name, button_position)


    def select_command(self, row):
        for i in range(self.command_count):
            button_area_start = (self.width // self.command_count) * i

            button_area_end = button_area_start + (self.width // self.command_count)

            if button_area_start <= row < button_area_end:

                return self.commands[i]
