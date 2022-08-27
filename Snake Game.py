import pygame, random, pygame_menu

#initialization pygame
pygame.init()

#defeined colors
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
orange = (255, 140, 0)

game_played = 0

(w,h) = (800, 800)

#creates the screen
root = pygame.display.set_mode((w,h))
#updates the screen
pygame.display.update()
pygame.display.set_caption('Snake Created By Aland')

ticks = pygame.time.Clock()

size = 10
speed = 25

font = pygame.font.SysFont(None, 30)

def Snake(size, snake_list):
    for i in snake_list:
        pygame.draw.rect(root, blue, [i[0], i[1], size, size])

def Dead_Page(msg, color):
    text_1 = font.render(msg, True, color)
    root.blit(text_1, [w/4, h/4])

def The_Score(score):
    username = name.get_value()
    text_2 = font.render(username, True, orange)
    root.blit(text_2, [0, 0])
    text_3 = font.render('Score: '+str(score), True, orange)
    root.blit(text_3, [0, 30])

def Game():
    running = False
    options = False

    #starting co-ordinates
    x = w/2
    y = h/2

    x_change = 0
    y_change = 0

    foodx = round(random.randrange(0, w - size) / 10) * 10
    foody = round(random.randrange(0, h - size) / 10) * 10

    snake_list = []
    length = 1

    while not running:

        while options == True:
            root.fill(white)
            Dead_Page('O No! You Died Q-Quit A-Play Again', red)
            The_Score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_a:
                        Game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #When close button is pressed close display
                running = True
            if event.type == pygame.KEYDOWN:
                #Make the snake go Up
                if event.key == pygame.K_DOWN:
                    y_change = 10
                    x_change = 0
                #Make the snake go Down
                elif event.key == pygame.K_UP:
                    y_change = -10
                    x_change = 0
                #Make the snake go Right
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                #Make the snake go Left
                elif event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0

        if x >= w or x < 0 or y >= h or y < 0:
            options = True

        x += x_change
        y += y_change
        root.fill(green)
        pygame.draw.rect(root, red, [foodx, foody, size, size])
        body = []
        body.append(x)
        body.append(y)
        snake_list.append(body)
        if len(snake_list) > length :
            del snake_list[0]
        #Snake cant over-lap itself
        for i in snake_list[:-1]:
            if i == body:
                options = True

        Snake(size, snake_list)

        pygame.display.update()

        if x ==foodx and y == foody:
            foodx = round(random.randrange(0, w - size) / 10) * 10
            foody = round(random.randrange(0, h - size) / 10) * 10
            length += 1
            print('Mmmm!!')
        ticks.tick(speed)

menu = pygame_menu.Menu('Welcome To My Snake Game', 800, 800, theme = pygame_menu.themes.THEME_BLUE)
name = menu.add.text_input('Username: ', Username = '')
menu.add.button('Play', Game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(root)
