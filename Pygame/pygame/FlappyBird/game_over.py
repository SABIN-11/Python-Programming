import pygame

pygame.init()

# screen dimensions
screen_WIDTH = 500
screen_HEIGHT = 400

# display surface
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption("Staring Phase")

# Clock for framerate
fps = 60    # frame per second
clock = pygame.time.Clock()

# Player / Rectangle
rect_WIDTH = rect_HEIGHT = 25.0
player = pygame.Rect((screen_WIDTH / 2) - (rect_WIDTH / 2), (screen_HEIGHT / 2 ) - (rect_HEIGHT / 2), rect_WIDTH, rect_HEIGHT)

# color for rectange
BLUE = (0, 0, 255)  # rgb value for blue
BLACK = (0, 0, 0)   # rgb value for black
WHITE = (255, 255, 255)

gravity = 0.15
upward_displacement = -7
player_movement = 0.0

running = True

has_started = False
flag = 0
inc_or_dec = 1


while running:

    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLUE, player)

    # Until user presses white space, just jiggle up and down forever
    if not has_started:
        player.centery += inc_or_dec
        flag += 1
        if flag == 10:
            inc_or_dec = -(inc_or_dec)
            flag = 0
    else:   # After user presses white space, then game starts
        player_movement += gravity
        player.centery += player_movement

        if player.top <= screen_rect.top or player.bottom >= screen_rect.bottom:
            player.centerx, player.centery = (screen_WIDTH / 2) - (rect_WIDTH / 2), (screen_HEIGHT / 2 ) - (rect_HEIGHT / 2)
            has_started = False
            


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                has_started = True
                player_movement = upward_displacement

    pygame.display.update()
    clock.tick(fps)




pygame.quit()