import sys
import pygame

class Square:
    def __init__(self, start_x, start_y):
        self.start_x,self.start_y = start_x,start_y
        self.new_x,self.new_y  = start_x,start_y
        self.change_x,self.change_y = 0,0
        self.drawing = False
        self.new_start_x,self.new_start_y = start_x,start_y
    def draw_square(self, screen, square_color):
        pygame.draw.rect(screen, square_color, (self.new_start_x, self.new_start_y, self.change_x, self.change_y), 5)
    def update_draw(self):
        if self.drawing:
            mouse_pos = pygame.mouse.get_pos()
            self.new_x,self.new_y = mouse_pos[0],mouse_pos[1]
            if self.new_x > self.start_x and self.new_y > self.start_y:
                self.change_x = self.new_x - self.start_x
                self.change_y = self.new_y - self.start_y
            elif self.new_x < self.start_x and self.new_y > self.start_y:
                self.new_start_x = self.new_x
                self.change_x = self.start_x - self.new_start_x
                self.change_y = self.new_y - self.start_y
            elif self.new_x < self.start_x and self.new_y < self.start_y:
                self.new_start_x = self.new_x
                self.new_start_y = self.new_y
                self.change_x = self.start_x - self.new_start_x
                self.change_y = self.start_y - self.new_start_y
            elif self.new_x > self.start_x and self.new_y < self.start_y:
                self.new_start_y = self.new_y
                self.change_x = self.new_x - self.start_x
                self.change_y = self.start_y - self.new_start_y
def run():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Ctrl+Z")
    bg_color = (0, 0, 0)
    square_color = (255, 255, 255)
    squares = []
    last_square_index = -1
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_mouse_pos = pygame.mouse.get_pos()
                new_square = Square(start_mouse_pos[0], start_mouse_pos[1])
                new_square.drawing = True
                squares.append(new_square)
                last_square_index += 1
            if event.type == pygame.MOUSEBUTTONUP:
                squares[last_square_index].drawing = False
            if keys[pygame.K_LCTRL] and keys[pygame.K_z] and len(squares) > 0:
                last_square_index -= 1
                squares.pop()
        if len(squares) > 0:
            squares[last_square_index].update_draw()
            squares[last_square_index].draw_square(screen, square_color)
        screen.fill(bg_color)
        for square in squares:
            square.draw_square(screen, square_color)
        pygame.display.update()
run()