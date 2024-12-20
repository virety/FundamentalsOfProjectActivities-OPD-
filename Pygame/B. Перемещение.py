import pygame
sc=pygame.display.set_mode((300,300))
clock=pygame.time.Clock()
x,y=0,0
fat,fps=20,30
pos=(x,y,fat,fat)
color=(255,255,255)
game=True
moving=False
while game:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
            moving = True
    if event.type == pygame.MOUSEMOTION:
        if moving:
            x_new, y_new = event.rel
            x, y = x + x_new, y + y_new
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        moving = False
    pygame.draw.rect(sc, color, (x, y, fat, fat))
    pygame.display.flip()
    sc.fill((0, 0, 0))
pygame.quit()