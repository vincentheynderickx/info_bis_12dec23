
import pygame
import random

pygame.init()




    
screen = pygame.display.set_mode( (width, height) )
clock = pygame.time.Clock()
pink = (249,66,158)
white = (255, 255, 255)
black = (0, 0, 0)
snake_size = 3
snake_speed = 10


square_size = 20
lines = 15
columns = 20


width = square_size * columns
height = square_size * lines

window = pygame.display.set_mode((width, height))


def draw_checkboard():
    for line in range(lines):
        for column in range(columns):
            if (line + column) % 2 == 0:
                color_case = white
            else:
                color_case = black
            pygame.draw.rect(window, color_case, (column * square_size, line * square_size, square_size, square_size))


draw_checkboard()




def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, pink, [x[0], x[1], snake_size, snake_size])




def gameLoop(): 
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    score = 0

    foodx = round(random.randrange(0, width - snake_size) / 10) * 10
    foody = round(random.randrange(0, height - snake_size) / 10) * 10

    while not game_over:

        while game_close == True:
            window.fill(black)
            our_snake(snake_block, snake_list)
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
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, pink, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            length_of_snake += 1
            score +=1
            pygame.display.set_caption('Score du Snake = ',score)
            snake_speed = snake_speed + 1


        clock.tick(snake_speed)

        

    pygame.quit()
    quit()


gameLoop()









