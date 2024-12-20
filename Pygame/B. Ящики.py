import pygame

def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapfile:
        level_map = [line.strip() for line in mapfile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
def load_image(image_filename):
    image = pygame.image.load(image_filename)
    return image
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png'),
    'broken': load_image('broken_box.png')  
}
player_image = load_image('mario.png')
tile_width = tile_height = 50
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.last_direction = None 
    def move(self, dx, dy):
        if 0 <= self.pos_x + dx < level_x and 0 <= self.pos_y + dy < level_y:
            new_x = self.pos_x + dx
            new_y = self.pos_y + dy
            if level[new_y][new_x] != '#':
                tiles_group.remove(next((sprite for sprite in tiles_group if
                                         sprite.rect.x == tile_width * new_x and sprite.rect.y == tile_height * new_y),
                                        None))
                self.rect.x += tile_width * dx
                self.rect.y += tile_height * dy
                self.pos_x = new_x
                self.pos_y = new_y
                if level[new_y][new_x] == '@':
                    tiles_group.add(Tile('empty', new_x, new_y))
                    level[new_y] = level[new_y][:new_x] + '.' + level[new_y][new_x + 1:]
            self.last_direction = (dx, dy)
    def break_box(self, pos_x, pos_y):
        if self.last_direction:
            dx, dy = self.last_direction
            new_x = pos_x + dx
            new_y = pos_y + dy
            if 0 <= new_x < level_x and 0 <= new_y < level_y and level[new_y][new_x] == '#':
                tiles_group.remove(next((sprite for sprite in tiles_group if
                                         sprite.rect.x == tile_width * new_x and sprite.rect.y == tile_height * new_y),
                                        None))
                level[new_y] = level[new_y][:new_x] + '.' + level[new_y][new_x + 1:]
                self.last_direction = None
                tiles_group.add(Tile('broken', new_x, new_y))
def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
level = load_level('map.txt')
player, level_x, level_y = generate_level(level)
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.break_box(player.pos_x, player.pos_y)
            elif event.key == pygame.K_UP:
                player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
            elif event.key == pygame.K_LEFT:
                player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    player_group.draw(screen) 
    pygame.display.flip()
pygame.quit()