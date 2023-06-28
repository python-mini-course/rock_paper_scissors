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


rock_img = pygame.image.load("./images/rock.png")
paper_img = pygame.image.load("./images/paper.png")
scissors_img = pygame.image.load("./images/scissors.png")

images = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissors": scissors_img
}

# choice
computerChoice = False
userChoice = False

# For winning & losing game (if won = True, user won; if lost = True, user lost)
won = False
lost = False
tied = False

while running:
    # fill the Display with a color to wipe away anything from last frame
    Display.fill("white")

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
            if key == "1" or key == "2" or key == "3":
                #computer choice
                computerChoice = whatIsIt(generateComputerChoice())
                userChoice = whatIsIt(int(key))

                # print tie if user and computer respose is the same
                if userChoice == computerChoice:
                    tied = True
                else: 
                    if userChoice == "Rock":
                        if computerChoice == "Scissors":
                            won = True
                        if computerChoice == "Paper":
                            lost = True
                    elif userChoice == "Scissors":
                        if computerChoice == "Paper":
                            won = True
                        if computerChoice == "Rock":
                            lost = True
                    elif userChoice == "Paper":
                        if computerChoice == "Rock":
                            won = True
                        if computerChoice == "Scissors":
                            lost = True
            
                # update the screen
                pygame.display.flip()
                # continue & do not execute any code beyond this point
                continue
    
    # Display title
    title = FONT.render('Rock Scissor Paper', True, BLACK)
    Display.blit(title, (400, 100))

    # Computer Text
    computerText = FONT.render("Computer", True, BLACK)
    Display.blit(computerText, (100, 500))

    # User Text
    userText = FONT.render("User", True, BLACK)
    Display.blit(userText, (800, 500))


    # Game Completed
    if won: # user won
        # display winning screen
        Display.blit(images[computerChoice], (100, 200))
        Display.blit(images[userChoice], (800, 200))
        wonText = FONT.render('YOU WON!!', True, BLACK)
        Display.blit(wonText, (900, 600))
    elif lost: # user lost
        # display losing screen
        Display.blit(images[computerChoice], (100, 200))
        Display.blit(images[userChoice], (800, 200))
        lostText = FONT.render('YOU LOST!!', True, BLACK)
        Display.blit(lostText, (900, 600))
    elif tied: # user tied
        # display losing screen
        Display.blit(images[computerChoice], (100, 200))
        Display.blit(images[userChoice], (800, 200))
        lostText = FONT.render('YOU TIED!!', True, BLACK)
        Display.blit(lostText, (900, 600))
    else:
        # Random Image
        randomChoice = whatIsIt(generateComputerChoice())
        Display.blit(images[randomChoice], (100, 200))

    # flip() the display to put your work on Display
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()