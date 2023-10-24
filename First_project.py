import pygame # Importing the python gaming library
from sys import exit # Import exit from the system library

pygame.init() # Initializing pygame
screen = pygame.display.set_mode((800,400)) # Defining the size of the screen/window
pygame.display.set_caption("LZ's First Game") # Defining the name on the window
clock = pygame.time.Clock() # Creating an object for frameratelimit



while True: # Loop to keep the window's appearance 
    for event in pygame.event.get(): # Loop for checking input from the user in case they want to quit the game
        if event.type == pygame.QUIT: # Checking event
            pygame.quit() # Quiting pygame
            exit() # Ending every functioning code
        
    pygame.display.update() # Updating window
    clock.tick(120) # limiting framerate to 120fps
