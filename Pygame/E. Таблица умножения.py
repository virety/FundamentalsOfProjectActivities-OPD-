import pygame
import math
pygame.init()
WIDTH, HEIGHT = 900, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('E. Таблица умножения')
radius = 400
center_x = WIDTH // 2 
center_y = HEIGHT // 2  
num_elements = 360  
running = True
multiplier = 1
paused = False
font = pygame.font.SysFont("Arial", 20)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
    win.fill((0, 0, 0))
    for i in range(num_elements):
        angle = i * (360 / num_elements) 
        rad_angle = math.radians(angle) 
        x = int(center_x + radius * math.cos(rad_angle)) 
        y = int(center_y + radius * math.sin(rad_angle))  
        next_num = (i * multiplier) % num_elements
        next_angle = next_num * (360 / num_elements)
        next_rad_angle = math.radians(next_angle)
        next_x = int(center_x + radius * math.cos(next_rad_angle))
        next_y = int(center_y + radius * math.sin(next_rad_angle))
        color = pygame.Color(i % 256, (i + 128) % 256, (i + 64) % 256)
        pygame.draw.line(win, color, (x, y), (next_x, next_y), 2)
        # font = pygame.font.SysFont("Arial", 20)
        # text = font.render(str(i), True, color)
        # text_rect = text.get_rect(center=(x, y))
        # win.blit(text, text_rect)
    if not paused:
        multiplier += 0.001
    multiplier_text = font.render("Множитель: " + str(round(multiplier, 1)), True, (255, 255, 255))
    multiplier_rect = multiplier_text.get_rect(bottomleft=(10, HEIGHT - 10))
    win.blit(multiplier_text, multiplier_rect)
    pygame.display.update()
    # pygame.time.delay(1)
pygame.quit()
