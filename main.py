import pygame, sys, random
from pygame.math import Vector2

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect =  pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            body_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen,(183,111,122),body_rect)

pygame.init()
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_num*cell_size,cell_num*cell_size))
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
