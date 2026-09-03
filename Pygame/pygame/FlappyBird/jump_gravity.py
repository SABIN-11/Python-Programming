# One of the component for flappy bird
# Main thing - keyboard input and smooth gravity
# gravity should increase exponentially and not linearly


import pygame

# Screen Width and Height
screen_WIDTH = 500.0
screen_HEIGHT = 400.0

# Screen / Display Surface
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))

# Clock for framerate
fps = 60    # frame per second
clock = pygame.time.Clock()

# Player / Rectangle
rect_WIDTH = rect_HEIGHT = 25.0
player = pygame.Rect((screen_WIDTH / 2) - (rect_WIDTH / 2), (screen_HEIGHT / 2 ) - (rect_HEIGHT / 2), rect_WIDTH, rect_HEIGHT)

# color for rectange
BLUE = (0, 0, 255)  # rgb value for blue
BLACK = (0, 0, 0)   # rgb value for black

# gravity
gravity = 0.25
player_downward_movement = 0.0  # for acceleration / exponential motion
upward_displacement = -7
max_downward_speed = 5

running = True

while running:

    screen.fill(BLACK)  # this is so that we won't get the previous frame

    pygame.draw.rect(screen, BLUE, player)

    player_downward_movement += gravity # player_downward_movement is always increasing
    player.centery += player_downward_movement

    # 1ST Method to take keyboard input is to use get_pressed() method
    # keys = pygame.key.get_pressed() # get all the keys and their current state whether they are presses(1) or not pressed(0)
    # if keys[pygame.K_SPACE]:
    #     player_downward_movement = upward_displacement

    # if player_downward_movement > max_downward_speed:
    #     player_downward_movement = max_downward_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 2ND Method to take keyboard input is to use event loop
        if event.type == pygame.KEYDOWN:    # KEYDOWN - key pressed and KEYUP - key released
            if event.key == pygame.K_SPACE: # If the pressed key is a spacebar
                player_downward_movement = upward_displacement

        # 3RD Method - mouse input 
        # if event.type == pygame.MOUSEBUTTONDOWN:    # Mouse button is pressed
        #     mouse_pos = event.pos # attribute to get the (x, y) position of the mouse
        #     if player.collidepoint(mouse_pos):
        #         player_downward_movement = upward_displacement


                  

        

    pygame.display.update() # for changes in the screen
    clock.tick(fps) # calculates the time for each frame and if time for frame is faster than boundary, then delay happens

pygame.quit()