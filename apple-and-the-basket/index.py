import pygame
import random
import math
#intialize the pygame
pygame.init()
from pygame import mixer

#create screen
screen = pygame.display.set_mode((800,600))
#Title and logo
pygame.display.set_caption("apple game")  
icon = pygame.image.load("apple.png")
pygame.display.set_icon(icon)

#background
background = pygame.image.load("bg.png")

#player
playerImg = pygame.image.load("basket.png")
playerX= 370
playerY = 480
playerX_change = 0

#apple

appleImg = pygame.image.load("apple.png")
appleX= random.randint(0,800)
appleY = random.randint(50,150)
appleX_change = 0


#score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10
def show_score(x,y):
    score = font.render("Score :" + str(score_value), True,(255,255,255))
    screen.blit(score,(x,y))


def player(x,y):
    screen.blit(playerImg,(x,y))

def apple(x,y):
    screen.blit(appleImg,(x,y))

def iscollision (appleX,apppleY,playerX,playerY):
    distance = math.sqrt((math.pow(appleX-playerX,2) )+ (math.pow(appleY-playerY,2)))
    if distance < 27:
        return True
    else :
        return False


#game loop
running = True
while running:
    #RGB       
    screen.fill((0,0,0))
    #background
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

        #if the keytroke is pressed check whether its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 1
    
    
    playerX += playerX_change
    appleY += 0.6
    if appleY >= 500:
        appleX= random.randint(0,800)
        appleY = random.randint(50,150)
        score_value -= 1
    if playerX <=0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
        
    #colliion
    collision = iscollision(appleX,appleY,playerX,playerY)
    if collision:
        appleY = 50
        apple_state = "ready"
        score_value += 1
        appleX= random.randint(0,800)
        appleY = random.randint(50,150)

    show_score(textX,textY)
    player(playerX,playerY)
    apple(appleX,appleY)
    pygame.display.update()
     