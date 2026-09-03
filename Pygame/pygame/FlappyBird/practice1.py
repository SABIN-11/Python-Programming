import pygame
from sys import exit
import random

pygame.init()

width = 800
height = 550

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Practice 1')

clock = pygame.time.Clock()
fps = 60

# background image
back_img = pygame.image.load('pygame/FlappyBird/backgroundFlappy.png').convert_alpha()
back_img = pygame.transform.scale(back_img, (width, height))

# ground
ground = pygame.image.load('pygame/FlappyBird/ground.png').convert_alpha()
ground = pygame.transform.scale(ground, (width, 50))
ground_rect = ground.get_rect(bottom = 550)

# player
player = pygame.image.load('pygame/FlappyBird/bird.png').convert_alpha()
player = pygame.transform.scale(player, (80, 80))
player_rect = player.get_rect(midtop = (350, 100))

# gravity = 0.499999  # doesn't work because 0.4999999 is truncated to 0 as Rect object only stores integer value
# gravity = 0.5   # works as it gets round off to 1
gravity = 0.25
player_movement = 0.0 # for smooth acceleration
upward_displacement = -7 # upward displacement - 7 pixels

# lower and upper boundary
lower_bound = screen.get_height() - ground.get_height() + 31   # difference between height of the screen and the ground
upper_bound = -11

# pipe image
pipe = pygame.image.load('pygame/FlappyBird/pipe.png').convert_alpha()
pipe = pygame.transform.scale(pipe, (350, 150))

pipe_vertical_gap = 100

top_pipe = pipe.get_rect(top = 0)
down_pipe = pipe.get_rect(bottom = height - ground.get_height())

top_pipe.x = down_pipe.x = 800

speed_for_pipe = 5

# score
font = pygame.font.SysFont(None, 25)
current_score = 0
score = font.render(f'Score: {current_score}', True, "Red")
score_rect = score.get_rect(midtop = (50, 20))

flag_score = True

# function to end the game
def end_the_game():
    pygame.quit()
    exit() 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_the_game()
        if event.type == pygame.KEYDOWN:    # if any key is pressed
            if event.key == pygame.K_SPACE: # and if that key is a spacebar
                player_movement = upward_displacement   # make the player_movement negative to move the player in upward direction

    screen.blit(back_img, (0, 0))

    ground_rect.x -= speed_for_pipe

    screen.blit(ground, ground_rect)
    screen.blit(ground, (ground_rect.x + width, ground_rect.y))

    screen.blit(score, score_rect)

    screen.blit(pipe, (top_pipe.x, 0)) # upper pipe
    top_pipe.x -= speed_for_pipe
 
    screen.blit(pipe, down_pipe)   # lower pipe
    down_pipe.x -= speed_for_pipe 

    # for downward acceleration
    player_movement += gravity
    player_rect.centery += player_movement  # when the player_movement is negative, then player_rect.centery is being decreased i.e moving upward
    # first player_movement is -(upward), then 0, then +(downward)
    
    screen.blit(player, player_rect)

    if ground_rect.right < 0:
        ground_rect.x = 0
        ground_rect.y = height - ground.get_height()
    
    if top_pipe.right < 0 and down_pipe.right < 0:
        flag_score = True
        top_pipe.x = down_pipe.x = 800
        down_pipe.y = height - ground.get_height() - 150 

    if player_rect.right > top_pipe.right and player_rect.right > top_pipe.right:
        if flag_score:
            current_score += 1
            flag_score = False
            score = font.render(f'Score: {current_score}', True, "Red")


    if player_rect.bottom >= lower_bound or player_rect.top <= upper_bound :
        print('GAME IS OVER')
        end_the_game()

    
    
    pygame.display.update()
    clock.tick(fps) # defining frame rate as 60 frames per second
