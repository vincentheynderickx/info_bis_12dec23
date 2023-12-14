import pygame
import random

pygame.init()

clock = pygame.time.Clock()
pink = (249,66,158)
white = (255, 255, 255)
black = (0, 0, 0)

square_size = 20
number_lines = 15
number_columns = 20
width = square_size * number_columns
height = square_size * number_lines

window = pygame.display.set_mode((width, height))

def draw_checkboard():
    for line in range(number_lines):
        for column in range(number_columns):
            if (line + column) % 2 == 0:
                color_case = white
            else:
                color_case = black
            pygame.draw.rect(window, color_case, (column * square_size, line * square_size, square_size, square_size))

draw_checkboard()

def our_snake(snake_size, snake_positions):
    for x in snake_positions:
        pygame.draw.rect(window, pink, [x[0], x[1], snake_size, snake_size])

def gameLoop(): 
    game_over = False
    game_close = False
    head_position = (width / 2 , height / 2)
    snake_direction=[-1,0]
    snake_size = 3
    snake_speed = 3
    snake_positions = []
    score = 0
    fruit_x = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
    fruit_y = round(random.randrange(0, height - snake_size) / 20.0) * 20.0

    while not game_over:
        while game_close == True:
            our_snake(snake_size, snake_positions)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction!=[1,0]:
                    snake_direction=[-1,0]
                elif event.key == pygame.K_RIGHT and snake_direction!=[-1,0]:
                    snake_direction=[1,0]
                elif event.key == pygame.K_UP and snake_direction!=[0,1]:
                    snake_direction=[0,-1]
                elif event.key == pygame.K_DOWN and snake_direction!=[0,-1]:
                    snake_direction=[0,1]

        if head_position[0] >= width or head_position[0] < 0 or head_position[1] >= height or head_position[1] < 0:
            game_close = True
        head_position[0] += snake_direction[0]
        head_position[1] += snake_direction[1]
        pygame.draw.rect(window, pink, [fruit_x*20, fruit_y*20, snake_size, snake_size])
        snake_head = []
        snake_head.append(head_position[0])
        snake_head.append(head_position[1])
        snake_positions.append(snake_head)
        if len(snake_positions) > snake_size:
            del snake_positions[0]

        for x in snake_positions[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_positions)

        pygame.display.update()

        if head_position[0] == fruit_x and head_position[1] == fruit_y:
            fruit_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            fruit_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_size += 1
            score +=1
            pygame.display.set_caption('Score du Snake = ',score)
            snake_speed = snake_speed + 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()