import pygame 
import random

pygame.init()

# screen dimensions
screen_WIDTH = 500
screen_HEIGHT = 400

# display surface
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption("Pillars Mechanism")

# background and ground
background = pygame.image.load('pygame/FlappyBird/backgroundFlappy.png')
background_scaled = pygame.transform.scale(background, (screen_WIDTH, screen_HEIGHT))
background_rect = background_scaled.get_rect()

ground_height = 70
ground_width = screen_WIDTH
ground = pygame.image.load('pygame/FlappyBird/ground.png')
ground_scaled = pygame.transform.scale(ground, (ground_width, ground_height))
ground_x = 0
ground_y = screen_HEIGHT - ground_height
ground_rect = ground_scaled.get_rect()

pillar_width = 180

pillar = pygame.image.load('pygame/FlappyBird/pipe.png')

clock = pygame.time.Clock()

def generate_pillars() -> tuple:

    top_pillar_scaled = pygame.transform.scale(pillar, (pillar_width, random.randint(80, 100)))
    bottom_pillar = pygame.transform.scale(pillar, (pillar_width, random.randint(80, 100)))
    bottom_pillar_scaled = pygame.transform.flip(bottom_pillar, False, True)

    return (top_pillar_scaled, bottom_pillar_scaled)

def generate_rect_for_pillars(top_pillar_scaled, bottom_pillar_scaled) -> tuple:
    top_pillar_rect = top_pillar_scaled.get_rect(x = screen_WIDTH, y = 0)
    bottom_pillar_rect = bottom_pillar_scaled.get_rect(bottomleft = (screen_WIDTH, screen_HEIGHT - ground_rect.height + 3))

    return (top_pillar_rect, bottom_pillar_rect)

time_interval = 1000    # 2000 millisecond i.e 2 second
previous_time = 0  # for maintaining constant time interval

speed = 5
pillar_pairs = []

running = True

while running:

    ground_x -= speed

    screen.blit(background_scaled, background_rect)
    screen.blit(ground_scaled, (ground_x, ground_y))
    screen.blit(ground_scaled, (ground_x + ground_width, ground_y))

    if ground_x <= -screen_WIDTH:
        ground_x = 0
    
    current_time = pygame.time.get_ticks()  # get the current millisecond since pygame.init() was called

    if current_time - previous_time > time_interval:
        previous_time = current_time
        top_pillar, bottom_pillar = generate_pillars()
        top_pillar_rect, bottom_pillar_rect = generate_rect_for_pillars(top_pillar, bottom_pillar)
        pillar_pairs.append((top_pillar, bottom_pillar, top_pillar_rect, bottom_pillar_rect))

    for pair in pillar_pairs:

        top_pillar, bottom_pillar, top_pillar_rect, bottom_pillar_rect = pair

        top_pillar_rect.x -= speed
        bottom_pillar_rect.x -= speed

        screen.blit(top_pillar, top_pillar_rect)
        screen.blit(bottom_pillar, bottom_pillar_rect)

        pillar_pairs = [
            (top_pillar, bottom_pillar, top_pillar_rect, bottom_pillar_rect)
            for (top_pillar, bottom_pillar, top_pillar_rect, bottom_pillar_rect) in pillar_pairs
            if top_pillar_rect.right > 0
        ]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)  # 60 fps

pygame.quit()