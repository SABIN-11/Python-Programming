import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))    # DISPLAY SURFACE

sky = pygame.image.load('images/sky.png').convert_alpha()
ground = pygame.image.load('images/ground.png').convert_alpha()

snail = pygame.image.load('images/snail.png').convert_alpha()

soldier = pygame.image.load('images/soldier.png').convert_alpha()

font = pygame.font.Font('font/pixeltype.ttf', 40)
text_surf = font.render("Score: 0", True, "red")   # It renders text in the surface, 3 arguments (text, anti-alias, color)
# anti-aliasing is a technique to smooth out those edges
# anti-alias takes True or False
# True - Smooth the edges
# False - crisper, jagged text

clock = pygame.time.Clock() # Instance of Clock Class
snail_x, snail_y = 800, 300
soldier_x = 0
score = 0
flag = True


while True:

    snail_rect = snail.get_rect(bottomright = (snail_x, snail_y))   
    # creating a rectange of same size as surface of snail
    # snail is a Surface object and get_rect is a method of Surface class
    # with the help of rectangle, we can use multiple points like topleft, bottomright, bottomleft, midtop, midbottom 
    # to position the surface rather than just topleft 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(snail, snail_rect)  # This simply means that snail surface should be positioned however the rectangle is positioned
    screen.blit(soldier, (soldier_x, 220))  
    screen.blit(text_surf, (350, 80))

    snail_x -= 3
    soldier_x += 3

    if snail_x < -50 and soldier_x > 810:
        snail_x = 800
        soldier_x = 0
        flag = True

    if snail_x <= soldier_x:
        if flag:
            score += 1
            flag = False
        text_surf = font.render(f"Score: {score}", True, "red") 

    pygame.display.update() # Update every frame to show changes to the user 
    clock.tick(60)
