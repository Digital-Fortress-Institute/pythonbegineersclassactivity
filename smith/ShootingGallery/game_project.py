import pygame
import math


pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font("C:/Users/SMITH/Desktop/gitpython/ShootingGallery/assets/font/myFont.ttf", 32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
guns = []


level = 1
for i in range(1,4):
    bgs.append(pygame.image.load(f"C:/Users/SMITH/Desktop/gitpython/ShootingGallery/assets/bgs/{i}.png"))
    banners.append(pygame.image.load(f"C:/Users/SMITH/Desktop/gitpython/ShootingGallery/assets/banners/{i}.png"))
    guns.append(pygame.image.load(f"C:/Users/SMITH/Desktop/gitpython/ShootingGallery/assets/guns/{i}.png"))

def draw_gun():
    mouse_pos = pygame.get_pos()
    gun_point = (WIDTH/2, HEIGHT - 200)
    lasers = ["red", "purple", "green"]
    clicks = pygame.mouse.get_pressed()
    if mouse_pos[0] != gun_point[0]:
        slope  = (mouse_pos[1] - gun_point[1])/(mouse_pos[0] - gun_point[0])
    else:
        slope = -100000
    angle = math.atan(slope)
    rotation = math.degrees(angle)




run = True
while run:
    timer.tick(fps)

    screen.fill("black")
    screen.blit(bgs[level - 1], (0, 0))
    screen.blit(banners[level - 1], (0, HEIGHT - 200))

    if level > 0:
        draw_gun()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()