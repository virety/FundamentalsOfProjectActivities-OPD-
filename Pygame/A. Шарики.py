import pygame
import random
pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites, balls)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.math.Vector2(random.randint(-5, 5), random.randint(-5, 5))
    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        if self.rect.left < 0 or self.rect.right > width:
            self.velocity.x = -self.velocity.x
        if self.rect.top < 0 or self.rect.bottom > height:
            self.velocity.y = -self.velocity.y
        for ball in balls:
            if ball != self:
                if self.rect.colliderect(ball.rect):
                    self.velocity.x = -self.velocity.x
                    self.velocity.y = -self.velocity.y
class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
for _ in range(5):
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    Ball(20, x, y)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            Ball(20, x, y)
    all_sprites.update()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
