import pygame
from random import randint
import os

pygame.init()
image_loaded = False
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
playing = False
pygame.font.init()
font = pygame.font.SysFont(None, 36)
pygame.display.set_caption("Death by DVD")
try:
    dvd_image = pygame.image.load(os.path.join("img", "dvd.png"))
    dvd_image = pygame.transform.scale(dvd_image, (50, 50))
    image_loaded = True
except:
    print("Image(s) Not Loaded!  Continuing as normal...")

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Emeny:
    x = 250 + randint(-20, 20)
    y = 250 + randint(-20, 20)
    vx = 3
    vy = -4

def init():
    one.x = 50
    one.y = 50
    two.x = 400
    two.y = 400
    Emeny.x = 250 + randint(-20, 20)
    Emeny.y = 250 + randint(-20, 20)
    Emeny.vx = 3
    Emeny.vy = -4

one = Player(0, 0)
two = Player(350, 350)


one_rect = pygame.draw.rect(screen, "red", (one.x, one.y, 100, 100))
two_rect = pygame.draw.rect(screen, "blue", (two.x, two.y, 100, 100))
ball_rect = pygame.draw.rect(screen, "white", (Emeny.x, Emeny.y, 50, 50))
if image_loaded:
    screen.blit(dvd_image, (Emeny.x, Emeny.y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    if playing:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            one.y = one.y - 15
        if keys[pygame.K_s]:
            one.y = one.y + 15
        if keys[pygame.K_a]:
            one.x = one.x - 15
        if keys[pygame.K_d]:
            one.x = one.x + 15
        
        if keys[pygame.K_UP]:
            two.y = two.y - 15
        if keys[pygame.K_DOWN]:
            two.y = two.y + 15
        if keys[pygame.K_LEFT]:
            two.x = two.x - 15
        if keys[pygame.K_RIGHT]:
            two.x = two.x + 15

        if one.x < 0:
            one.x = 0
        if one.y < 0:
            one.y = 0
        if one.x > 400:
            one.x = 400
        if one.y > 400:
            one.y = 400

        if two.x < 0:
            two.x = 0
        if two.y < 0:
            two.y = 0
        if two.x > 400:
            two.x = 400
        if two.y > 400:
            two.y = 400

        Emeny.x = Emeny.x + Emeny.vx
        Emeny.y = Emeny.y + Emeny.vy

        if Emeny.x < 0 or Emeny.x > 450:
            Emeny.vx = -Emeny.vx
        if Emeny.y < 0 or Emeny.y > 450:
            Emeny.vy = -Emeny.vy

        if one_rect.colliderect(two_rect) or one_rect.colliderect(ball_rect) or two_rect.colliderect(ball_rect):
            playing = False


        one_rect = pygame.draw.rect(screen, "red", (one.x, one.y, 100, 100))
        two_rect = pygame.draw.rect(screen, "blue", (two.x, two.y, 100, 100))
        ball_rect = pygame.draw.rect(screen, "white", (Emeny.x, Emeny.y, 50, 50))
        if image_loaded:
            screen.blit(dvd_image, (Emeny.x, Emeny.y))


    else:
        text = font.render("Press Space To Play!", True, (255, 255, 255))
        screen.blit(text, (130, 220))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            init()
            playing = True



    pygame.display.flip()
    clock.tick(60)

pygame.quit()