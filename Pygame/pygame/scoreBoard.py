import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((500, 300), pygame.RESIZABLE, pygame.VIDEORESIZE)
pygame.display.set_caption("Score Board")
clock = pygame.time.Clock() # Instance of Clock Class

# Image Surfaces
sky = pygame.image.load('images/sky.png').convert_alpha()
sky_rect = sky.get_rect(topleft = (0, 0))

ground = pygame.image.load('images/ground.png').convert_alpha()
ground_rect = ground.get_rect(topleft = (0, 200))

snail = pygame.image.load('images/snail.png').convert_alpha()
player = pygame.image.load('images/player.png').convert_alpha()

# Text Surface
score = 0
font = pygame.font.SysFont('georgia', 25)
text = font.render(f"Score: {score}", True, "red")
# It renders text in the surface, 3 arguments (text, anti-alias, color)
# anti-aliasing is a technique to smooth out those edges
# anti-alias takes True or False
# True - Smooth the edges
# False - crisper, jagged text
text_rect = text.get_rect(midtop = (250, 30))

# variables
# snail_x, snail_y = 500, 200
# player_x, player_y = 0, 200

# snail_rect = snail.get_rect(bottomright = (snail_x, snail_y))
# player_rect = player.get_rect(bottomleft = (player_x, player_y))

# creating a rectange of same size as surface of snail and player
# snail and player is a Surface object and get_rect is a method of Surface class
# with the help of rectangle, we can use multiple points like topleft, bottomright, bottomleft, midtop, midbottom 
# to position the surface rather than just topleft 
snail_rect = snail.get_rect(bottomright = (500, 200))
player_rect = player.get_rect(bottomleft = (0, 200))

flag_for_score = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Instead of creating rectangle for snail and player in each frame, just change the value of tuple of
    # respected position
    # snail_x -= 2
    # player_x += 2 
    snail_rect.x -= 2
    player_rect.x += 2

    # snail_rect.bottomright = (snail_x, snail_y)
    # player_rect.bottomleft = (player_x, player_y)

    screen.blit(sky, sky_rect)  # This simply means that snail surface should be positioned however the rectangle is positioned
    screen.blit(ground, ground_rect)    # This simply means that snail surface should be positioned however the rectangle is positioned
    screen.blit(snail, snail_rect)  # This simply means that snail surface should be positioned however the rectangle is positioned
    screen.blit(player, player_rect)    # This simply means that snail surface should be positioned however the rectangle is positioned
    screen.blit(text, text_rect)    # This simply means that snail surface should be positioned however the rectangle is positioned


    # if snail_x <= player_x:
    #     if flag_for_score:
    #         score += 1
    #         text = font.render(f"Score: {score}", True, "red")
    #         flag_for_score = False

    if snail_rect.colliderect(player_rect):
        if flag_for_score:
            score += 1
            text = font.render(f"Score: {score}", True, "red")
            flag_for_score = False

    if snail_rect.right < 0 and player_rect.left > 500:
        # snail_x, player_x = 500, 0
        snail_rect.x, player_rect.x = 500, 0
        flag_for_score = True

    # mouse_pos = pygame.mouse.get_pos()    # get the position of the mouse
    # if snail_rect.collidepoint(mouse_pos):    # if the point is present inside the rectangle or not
    #     print('hello')



    pygame.display.update() # Update every frame to show changes to the user 
    clock.tick(60)  # Framerate is bounded to 60fps

    

    


