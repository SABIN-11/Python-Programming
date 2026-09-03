import pygame   # Importing the pygame module which contains all other sub modules like display, event etc
from sys import exit

pygame.init()   # Initializing all the sub-modules, basically calling the init method of all the sub-modules

screen = pygame.display.set_mode((900, 600))    # display sub module has a method called set_mode which defines a window with 400 width and 300 height
# set_mode returns a Surface object, Surface is a class which encapsulates methods like fill() to draw in the window defined by set_mode
# So basically, set_mode defines a drawing board and it gives color brush to draw in that board

pygame.display.set_caption("FIRST WINDOW")  # Title of the window
clock = pygame.time.Clock() # It creates an instance of Clock Class

# CREATING A REGULAR SURFACE
reg_surf_1 = pygame.Surface((100, 50))   # We have to use Surface Class to create a regular object
reg_surf_2 = pygame.Surface((100, 50))   # We have to use Surface Class to create a regular object
reg_surf_3 = pygame.Surface((100, 50))   # We have to use Surface Class to create a regular object
reg_surf_4 = pygame.Surface((100, 50))   # We have to use Surface Class to create a regular object

reg_surfaces = [reg_surf_1, reg_surf_2, reg_surf_3, reg_surf_4]

running = True  # Just a variable to represent True

# note: 1 while loop equals to 1 frame
while running:  # While running is True, the loop continues
    
    # Everthing like drawing or event handling happens inside this while loop
    for event in pygame.event.get():    # event is another sub module, get() method returns a list of events like (key press, mouse move, quit event, etc.)
        if event.type == pygame.QUIT:   # type is an attribute that contains a integer, QUIT is a constant 256
            running = False # when we press (X), a QUIT event is queued in event.get() in the list

    screen.fill("lightblue")
    # pygame.draw.line(screen, "red", (0, 0), (400, 300))
    # pygame.draw.line(screen, "black", (400, 0), (0, 300))
    # reg_surf_1.fill("red"), 
    # screen.blit(reg_surf_1, (200, 100))   # Unless we add the regular surface in the display surface, it won't be visible
    # blit - block image transfer
    for regular in reg_surfaces:
        regular.fill("red")
    screen.blit(reg_surf_1, (0, 0))
    screen.blit(reg_surf_2, (900 - 100, 0))
    screen.blit(reg_surf_3, (900 - 100, 600 - 50))
    screen.blit(reg_surf_4, (0, 600 - 50))


    pygame.display.update() # updates the screen after everything is done for 1 frame
    clock.tick(60)  # It defines a ceiling for maximum frame rate
    # framerate - it means in 1 second how many images are being rendered
    # ceiling - tick(60) means in any device the maximum framerate is 60 frames per second
    # that means we can't go beyond 60fps like 70fps or 80fps
    # clock.tick() method calculates how much time it took for that while loop to come upto clock.tick()
    # and if took less than 16.67ms, it will delay for some time so that in 16.67ms, there is 1 frame being rendered
    # but if it takes more than 16.67 like 20ms, then it can't magically shorten the time so it just doesn't delay
    # thus, floor can't be set with a single method like tick()

        
pygame.quit()
exit()
