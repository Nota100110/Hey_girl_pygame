import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)

car_width = 91

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Hey girl')
clock = pygame.time.Clock()

carImg = pygame.image.load('Race_car_alpha.png')

def obstacles_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDispay.blit(text,(0,0))

def obstacle(obstaclex, obstacley, obstaclew, obstacleh, color):
    pygame.draw.rect(gameDisplay, color, [obstaclex, obstacley, obstaclew, obstacleh])

    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('YOU CRASHED!!')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.7)

    x_change = 0

    obstacle_startx = random.randrange(0, display_width)
    obstacle_starty = -600
    obstacle_speed = 7
    obstacle_width = 100
    obstacle_height = 100

    obstacleCount = 1
    
    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        # obstacle(obstaclex, obstacley, obstaclew, obstacleh, color)
        obstacle(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height, red)

        obstacle_starty += obstacle_speed
        car(x,y)
        obstacles_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if obstacle_starty > display_height:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(0,display_width)
            dodged += 1
            obstacle_speed += 1
            obstacle_width += (dodged * 1.2)

        
        if y < obstacle_starty+obstacle_height:
            print('y crossover')

            if x > obstacle_startx and x < obstacle_startx + obstacle_width or x+car_width > obstacle_startx and x + car_width < obstacle_startx+obstacle_width:
                print('x crossover')
                crash()
        
        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
