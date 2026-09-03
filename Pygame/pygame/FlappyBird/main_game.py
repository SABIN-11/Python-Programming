# creating flappy bird game

import pygame
import random   # for random heights of the pillars

# defining rgb values of colors
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)
RED        = (255, 0, 0)
GREEN      = (0, 255, 0)
BLUE       = (0, 0, 255)
YELLOW     = (255, 255, 0)

pygame.init()   # initializing all the sub modules in pygame

# screen dimensions
screen_WIDTH = 500
screen_HEIGHT = 400

# creating a screen surface
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
screen_rect = screen.get_rect() # rectange of the screen with that screen's dimension

pygame.display.set_caption("Flappy Bird: Dupli")

clock = pygame.time.Clock() # for maintaining frame rate
fps = 60    # 60 frames per second is the ceiling / boundary

# image loading
def load_image(file_path: str):
    return pygame.image.load(file_path)

# Step 1: Load Background, Ground and Player

# background
background = load_image('pygame/FlappyBird/backgroundFlappy.png')
background_scaled = pygame.transform.scale(background, (screen_WIDTH, screen_HEIGHT))


# ground
ground_height = 70
ground = load_image('pygame/FlappyBird/ground.png')
ground_scaled = pygame.transform.scale(ground, (screen_WIDTH, ground_height))
ground_rect = ground_scaled.get_rect()

ground_motion = 5   # decrease x value of ground by 5 in each frame

# positioning the top left part of the ground
ground_x = 0
ground_y = screen_HEIGHT - ground_height

# player
player_height = player_width = 60

player = load_image('pygame/FlappyBird/bird.png')
player_scaled = pygame.transform.scale(player, (player_width, player_height))
player_rect = player_scaled.get_rect(center = (screen_WIDTH / 2, screen_HEIGHT / 2))

# gravity
gravity = 0.25
player_movement = 0 # for smooth acceleration
upward_displacement = -5    # for keyboard input

# upper and lower boundary
upper_boundary = -5
lower_boundary = screen_HEIGHT - ground_height + 20

# flag to check if user has started the game or not
game_started = False

# initial stage of the bird before starting the game
increase_or_decrease = 1    # player will go up and down automatically initially
flag = 0    # to keep track of the unit up or down the player has moved so that we can decide whether to move player up or down next
area_to_move = 10

# score

current_score = 0
font = pygame.font.SysFont('georgia', 25)
score = font.render(f'Score: {current_score}', True, RED)
score_rect = score.get_rect(top = 10)

has_passed_pillar = True

# pillars

time_interval = 1000 # 1000 milliseconds time interval for generating each pair of top and bottom pillars
previous_time = 0   # for balancing the time_interval

pillar = load_image('pygame/FlappyBird/pillar.png')
pillar_width = 200

pillar_pair = []    # list of tuples of top and bottom pillars and their rectangles

def generate_pillars() -> tuple:
    top_pillar = pygame.transform.scale(pillar, (pillar_width, random.randint(100, 120))) # pillar at the top
    bottom = pygame.transform.scale(pillar, (pillar_width, random.randint(100, 120))) # pillar at the bottom
    bottom_pillar = pygame.transform.flip(bottom, False, True)  # Flip Vertically Not Horizontally

    return (top_pillar, bottom_pillar)

def rect_pillars(top_pillar, bottom_pillar) -> tuple:

    top_pillar_rect = top_pillar.get_rect(x = screen_WIDTH, y = 0)
    bottom_pillar_rect = bottom_pillar.get_rect(bottomleft = (screen_WIDTH, screen_HEIGHT - ground_height))

    return (top_pillar_rect, bottom_pillar_rect)

running = True

while running:  

    ground_x -= ground_motion

    screen.blit(background_scaled, (0, 0))
    screen.blit(ground_scaled, (ground_x, ground_y))    # our first ground that will be blitted to the screen surface
    screen.blit(ground_scaled, (ground_x + screen_WIDTH, ground_y)) # as soon as the first ground go out of the screen, new ground will come from the back

    if ground_x <= -screen_WIDTH:   # if first ground is already out of the screen then re-enter it again from the back
        ground_x = 0

    screen.blit(player_scaled, player_rect)

    if game_started:

        screen.blit(score, score_rect)
        player_movement += gravity
        player_rect.centery += player_movement

        current_time = pygame.time.get_ticks()  # get the time in milliseconds since pygame.init()
        
        if current_time - previous_time >= time_interval:

            previous_time = current_time
            top_pillar, bottom_pillar = generate_pillars()  # unpacking the tuple
            top_pillar_rect, bottom_pillar_rect = rect_pillars(top_pillar, bottom_pillar)  # unpacking the tuple
            pillar_pair.append([top_pillar, bottom_pillar, top_pillar_rect, bottom_pillar_rect, False])

        for pair in pillar_pair:
            top_pillar, bottom_pillar, top_pillar_rect, bottom_pillar_rect, passed = pair   # unpacking the tuple in the list

            screen.blit(top_pillar, top_pillar_rect)    # blitting the top pillar on the screen
            screen.blit(bottom_pillar, bottom_pillar_rect)  # # blitting the bottom pillar on the screen

            top_pillar_rect.x -= ground_motion  # moving the top pillar with the same velocity as ground
            bottom_pillar_rect.x -= ground_motion #  # moving the top pillar with the same velocity as ground

            if player_rect.left > top_pillar_rect.right and not passed:

                pair[4] = True
                current_score += 1
                score = font.render(f'Score: {current_score}', True, RED)
                screen.blit(score, score_rect)

            # if a pillar is already out of the screen from the left, then simply remove it from the list
            pillar_pair = [
                [top_pillar, bottom_pillar, top_pillar_rect, bottom_pillar_rect, passed]
                for [top_pillar, bottom_pillar, top_pillar_rect, bottom_pillar_rect, passed] in pillar_pair if top_pillar_rect.right > 0
            ]
        
        # Check collision between player and pillars
        for pair in pillar_pair:
            top_pillar_rect = pair[2]
            bottom_pillar_rect = pair[3]

            # if player_rect.colliderect(top_pillar_rect) or player_rect.colliderect(bottom_pillar_rect):
            #     game_started = False
            #     player_rect.centery = screen_HEIGHT / 2
            #     pillar_pair.clear()
            #     current_score = 0
            #     score = font.render(f'Score: {current_score}', True, RED)


        # checking if there is collision between player and top or player and ground
        if player_rect.top <= upper_boundary or player_rect.bottom >= lower_boundary:
            game_started = False
            player_rect.centery = screen_HEIGHT / 2
            current_score = 0
            score = font.render(f'Score: {current_score}', True, RED)


    else:
        player_rect.centery += increase_or_decrease # just increase the y of player
        flag += 1   # for checking in if condition

        if flag == area_to_move:    # if we have already moved up to our defined motion
            flag = 0
            increase_or_decrease = -(increase_or_decrease)


    for event in pygame.event.get():    # get() returns the list of the events that happens and if we press exit, then that event also gets stored inside the list
        if event.type == pygame.QUIT:   # pygame.QUIT = 256, an integer defining an exit event
            running = False
        if event.type == pygame.KEYDOWN:    # if a key is pressed
            if event.key == pygame.K_SPACE: # and that pressed key is a spacebar
                game_started = True
                player_movement = upward_displacement   # then make player_movement negative for upward motion of the player

    pygame.display.update() # to update our main screen surface in every frame
    clock.tick(fps) # maintains the frame rate of 60 fps

pygame.quit()   # deinitialize the sub modules
 
