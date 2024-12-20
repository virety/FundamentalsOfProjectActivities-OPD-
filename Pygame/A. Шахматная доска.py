import pygame as pg

pg.init()
run=True
clock=pg.time.Clock()
FPS=10
BLACK=(0,0,0)
WHITE=(255,255,255)
W,N=map(int,input().split())
WINDOW_SIZE=(W,W)
CELL_QTY=N
CELL_SIZE=W/N
pg.display.set_mode(WINDOW_SIZE)
COLORS=[BLACK,WHITE]
screen=pg.display.set_mode(WINDOW_SIZE)
screen.fill(BLACK)
is_even_qty=(N>0)
cell_color_index=0 if (is_even_qty) else 1
for y in range(CELL_QTY):
    for x in range(CELL_QTY):
        pg.draw.rect(screen,COLORS[cell_color_index] ,(x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE))
        cell_color_index^=True
    cell_color_index=cell_color_index^True if(is_even_qty) else cell_color_index
pg.display.update()
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            # pg.quit()
            run=False
    clock.tick(FPS)
pg.quit()