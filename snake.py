
import pygame


pygame.init()

screen = pygame.display.set_mode( (width, height) )
clock = pygame.time.Clock()

while True:

    # Wait one second, starting from last display or now
    clock.tick(1)


screen.fill( (0, 255, 0) )
pygame.quit()