import pygame
import sys
from random import randrange
class Cell:
    def __init__(self, x, y, cell_color, cell_size):
        self.x = x
        self.y = y
        self.cell_color = cell_color
        self.cell_size = cell_size
        self.center = (cell_size // 2 + x - 5, cell_size // 2 + y - 10)
        self.counter_mines = 0
    def draw_cell(self, screen):
        pygame.draw.rect(screen, self.cell_color, (self.x, self.y, self.cell_size, self.cell_size), 1)
class Mine(Cell):
    def draw_cell(self, screen):
        pygame.draw.rect(screen, self.cell_color, (self.x, self.y, self.cell_size, self.cell_size))
class MineField:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = int(screen_width / 10)
        self.all_cells = []
        self.mines_coors = []
        self.checked_cells = []
    def cells_generator(self, cell_color, mine_color):
        self.all_cells.append([0] * 12)
        for x in range(0, self.screen_width, self.cell_size):
            new_row = []
            for y in range(0, self.screen_height, self.cell_size):
                if (x, y) in self.mines_coors:
                    new_mine = Mine(x, y, mine_color, self.cell_size)
                    new_row.append(new_mine)
                else:
                    new_cell = Cell(x, y, cell_color, self.cell_size)
                    new_row.append(new_cell)
            new_row.append(0)
            new_row.insert(0, 0)
            self.all_cells.append(new_row)
        self.all_cells.append([0] * 12)
    def mines_coors_generator(self):
        while len(self.mines_coors) < 10:
            x = randrange(0, 10)
            y = randrange(0, 10)
            if (x, y) not in self.mines_coors:
                self.mines_coors.append((x * self.cell_size, y * self.cell_size))
    def checking_mines(self):
        mouse_pos = pygame.mouse.get_pos()
        row_index = mouse_pos[0] // self.cell_size + 1
        cell_index = mouse_pos[1] // self.cell_size + 1
        if type(self.all_cells[row_index][cell_index]) != Mine:
            if self.all_cells[row_index][cell_index] not in self.checked_cells:
                for row in range(row_index - 1, row_index + 2):
                    for cell in range(cell_index - 1, cell_index + 2):
                        if type(self.all_cells[row][cell]) == Mine:
                            self.all_cells[row_index][cell_index].counter_mines += 1
                self.checked_cells.append(self.all_cells[row_index][cell_index])
screen_width = 400
screen_height = 400
bg_color = (0, 0, 0)
cell_color = (255, 255, 255)
mine_color = (255, 0, 0)
def render_text(screen, font_color, x, y, message):
    pygame.font.init()
    my_font = pygame.font.SysFont("Arial", 20)
    text_surface = my_font.render(message, False, font_color)
    screen.blit(text_surface, (x, y))
def render_checked_cells(screen, checked_cells):
    for checked_cell in checked_cells:
        message = str(checked_cell.counter_mines)
        render_text(screen, cell_color, checked_cell.center[0], checked_cell.center[1], message)
def render_all_cells(screen, all_cells):
    screen.fill(bg_color)
    for row in all_cells[1:11]:
        for cell in row[1:11]:
            cell.draw_cell(screen)
def run():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Semi-Saper")
    field = MineField(screen_width, screen_height)
    field.mines_coors_generator()
    field.cells_generator(cell_color, mine_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                field.checking_mines()
        render_all_cells(screen, field.all_cells)
        render_checked_cells(screen, field.checked_cells)
        pygame.display.update()
run()
