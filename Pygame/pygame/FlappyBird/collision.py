import pygame, random

# screen dimensions
screen_WIDTH = 500
screen_HEIGHT = 400

# display surface
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
pygame.display.set_caption("COLLISION OF RECTANGLES")

# defining colors
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)
RED        = (255, 0, 0)
GREEN      = (0, 255, 0)
BLUE       = (0, 0, 255)
YELLOW     = (255, 255, 0)

rect_WIDTH = rect_HEIGHT = 25

def create_obstacles():
    return pygame.Rect(random.randint(0, screen_WIDTH - rect_WIDTH), random.randint(0, screen_HEIGHT - rect_HEIGHT), rect_WIDTH, rect_HEIGHT)

# main rectangle
rec1 = pygame.Rect(0, 0, rect_WIDTH, rect_HEIGHT)
# rec2 = create_obstacles()   # another rectangle for ----- (1)

# obstacles
# for ----- (2)
obstacles = []  # empty list for storing the rectangles
no_of_obstacles = 15

for i in range (no_of_obstacles + 1):
    obstacles.append(create_obstacles())    # append all the rectangles in the list

running = True

while running:

    screen.fill(BLACK)
    col = WHITE

    # collision with just 2 rectangles ----- (1)

    # mouse_pos = pygame.mouse.get_pos()  # get the co-ordinates of mouse
    # rec1.center = mouse_pos # this will help us move the rectange along with the mouse

    # # RETURNS 1 if rec1 and rec2 intersects
    # # OTHERWISE RETURNS 0
    # if rec1.colliderect(rec2):
    #     col = RED
    
    # pygame.draw.rect(screen, col, rec1)
    # pygame.draw.rect(screen, GREEN, rec2)

    # collision with multiple rectanges ----- (2)

    # mouse_pos = pygame.mouse.get_pos()  # get the co-ordinates of mouse
    # rec1.center = mouse_pos # this will help us move the rectange along with the mouse

    # # first way - manually
    # # for obstacle in obstacles:
    # #     if rec1.colliderect(obstacle):
    # #         col = RED

    # # second way - using built-in collidelist() method
    # # Returns the index of the rectance in the list obstacles if collided
    # # Returns -1 if no collision is found.
    # if rec1.collidelist(obstacles) >= 0:
    #     col = RED

    # pygame.draw.rect(screen, col, rec1)

    # for obstacle in obstacles:
    #     pygame.draw.rect(screen, GREEN, obstacle)

    # collision with points ----- (3)
    # mouse_pos = pygame.mouse.get_pos()  # get the co-ordinates of mouse
    
    # using collidepoint() method which checks if a point is inside a rectangle or not
    # True if point is inside the rect
    # False otherwise
    # for obstacle in obstacles:
    #     if obstacle.collidepoint(mouse_pos):
    #         pygame.draw.rect(screen, RED, obstacle)
    #     else:
    #         pygame.draw.rect(screen, GREEN, obstacle)

    # collision with lines ----- (4)
    mouse_pos = pygame.mouse.get_pos()  # get the co-ordinates of mouse which is the ending position of the line segment
    line_start = (screen_WIDTH / 2, screen_HEIGHT / 2)  # starting position of the line segment is the center of the screen

    pygame.draw.line(screen, WHITE, line_start, mouse_pos, 5)

    for obstacle in obstacles:
        if obstacle.clipline(line_start, mouse_pos):
            pygame.draw.rect(screen, RED, obstacle)
        else:
            pygame.draw.rect(screen, GREEN, obstacle)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()