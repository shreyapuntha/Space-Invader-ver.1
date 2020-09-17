import pygame
import random
import math
from pygame import mixer

pygame.init()


def player(x, y):
    screen.blit(playr, (x, y))


def enemy(x, y):
    screen.blit(enemyimg[i], (x, y))


def bulletfire(x, y):
    screen.blit(bulletimg, (x, y))


def collision(ax, ay, bx, by):
    d = math.sqrt(math.pow(ax - bx, 2) + math.pow(ay - by, 2))
    if d <= 30:
        col = True
    else:
        col = False
    return col


def got():
    ot = ofont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(ot, (200, 250))


playr = pygame.image.load('player.png')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("caption")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('backg.jpg')
bulletimg = pygame.image.load('bullet.png')
laser = mixer.Sound('lase.wav')
playerx = float(364)
playery = 500
pchange = 0
enemyimg = []
ey = []
ex = []
echange = []
noe = 3
for i in range(noe):
    ey.append(100)
    enemyimg.append(pygame.image.load('enemy.png'))
    ex.append(random.randint(0, 764))
    echange.append(2)

font = pygame.font.Font('freesansbold.ttf', 32)
ofont = pygame.font.Font('freesansbold.ttf', 64)
scr = 0
bt = False
bc = 0
by = 500
bx = 0
neg = -1
running = True
while running:
    screen.blit(background, (0, 0))
    player(playerx, playery)
    if bt == True:
        bulletfire(bx, by)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pchange = -2

            if event.key == pygame.K_RIGHT:
                pchange = 2
            if event.key == pygame.K_SPACE:
                if bt == False:
                    bx = playerx
                    bt = True
                    laser.play()
        if event.type == pygame.KEYUP:
            pchange = 0
    if playerx <= 0:
        playerx = 0
    if playerx >= 764:
        playerx = 764
    for i in range(noe):
        if ey[i] > 400:
            for j in range(noe):
                ey[j] = 2000
            got()

        if ex[i] <= 0 or ex[i] >= 764:
            echange[i] = echange[i] * neg
            ey[i] += 36
        ex[i] += echange[i]
        enemy(ex[i], ey[i])
        if collision(ex[i], ey[i], bx, by) == True:
            bt = False
            bc = 0
            by = 500
            ey[i] = 100
            ex[i] = random.randint(0, 764)
            scr += 1

    if by == 0:
        bt = False
        bc = 0
        by = 500
    if bt == True:
        bc = -4

    score = font.render("SCORE: " + str(scr), True, (255, 255, 255))
    screen.blit(score, (0, 0))

    by += bc
    playerx += pchange
    pygame.display.update()
