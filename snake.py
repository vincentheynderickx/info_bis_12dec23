
import pygame


pygame.init()

screen = pygame.display.set_mode( (width, height) )
clock = pygame.time.Clock()
rose = (249,66,158)
snake_size = 8

while True:

    # Wait one second, starting from last display or now
    clock.tick(1)

# Process new events (keyboard, mouse)
for event in pygame.event.get():
    pass # do nothing for the moment

def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, rose, [x[0], x[1], snake_size, snake_size])

screen.fill( (0, 255, 0) )
pygame.quit()