# pygame setup
import pygame

pygame.init()
Display = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# import helper functions
from helper import *

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (200,200,200)

# fonts
FONT = pygame.font.SysFont('Roboto', 80)

# center location in display
center = pygame.Vector2(Display.get_width() / 2, Display.get_height() / 2)

# For winning & losing game (if won = True, user won; if lost = True, user lost)
won = False
lost = False

while running:
    # Event listeners
    for event in pygame.event.get():

        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False

        # Get user input
        if event.type == pygame.KEYDOWN:
            # key is user input (if user press "s", key = "s")
            key = event.unicode

            # DO SOMETHING WITH KEY HERE
            # For example
            if key.isalpha(): # if key is a character
              # show black screen
              Display.fill("black")
              # update the screen
              pygame.display.flip()
              # continue & do not execute any code beyond this point
              continue

            if key.isnumeric(): # if key is a number
              # show red screen
              Display.fill("red")
              # update the screen
              pygame.display.flip()
              # continue & do not execute any code beyond this point
              continue
    
    # Game Completed
    if won: # user won
        # display winning screen
        Display.fill("white")
        wonText = FONT.render('YOU WON!!', True, BLACK)
        Display.blit(wonText, center)
        pygame.display.flip()
        continue
    if lost: # user lost
        # display losing screen
        Display.fill("white")
        lostText = FONT.render('YOU LOST!!', True, BLACK)
        Display.blit(lostText, center)
        pygame.display.flip()
        continue
                        

    # fill the Display with a color to wipe away anything from last frame
    Display.fill("white")

    # Display title
    title = FONT.render('The Game', True, BLACK)
    Display.blit(title, (500, 275))

    # Draw a rectangle (surface, color, point positions(x position, y position, x-length, y-length), width)
    pygame.draw.rect(Display, BLACK, (250, 200, 800, 200), 8)

    # Draw a line (surface, color, start position, end position, width)
    pygame.draw.line(Display, BLACK, (200,600),(1100,600),8)
    
    # flip() the display to put your work on Display
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()