import pygame # Importing the python gaming library
from sys import exit # Import exit from the system library

pygame.init() # Initializing pygame
screen = pygame.display.set_mode((800,400)) # Defining the size of the screen/window
pygame.display.set_caption("LZ's First Game") # Defining the name on the window
clock = pygame.time.Clock() # Creating an object for frameratelimit
test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf',50) # pygame.font.Font(font type, font size )
snail_surface = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha() # Importing snail image <convert_alpha means that when converting the image to a easier picture it will keep the original values such as png
sky_surface = pygame.image.load('UltimatePygameIntro-main\graphics\Sky.png').convert() # Importing sky picture for background
ground_surface = pygame.image.load('UltimatePygameIntro-main\graphics\ground.png').convert() # Importing ground picture for the ground
text_surface = test_font.render("My Game",False,"Black") # teste_font.render(text, AA, color) <AA means anti-aliasing, which is to smooth the edges of the text>
snail_x_position = 800 # Defining the starting position of the snail

while True: # Loop to keep the window's appearance 
    for event in pygame.event.get(): # Loop for checking input from the user in case they want to quit the game
        if event.type == pygame.QUIT: # Checking event
            pygame.quit() # Quiting pygame
            exit() # Ending every functioning code
    
    screen.blit(sky_surface,(0,0)) # Screen.blit(surface escolhida, (posicao))
    screen.blit(ground_surface,(0,300)) # Defining the position of the ground
    screen.blit(text_surface,(300,50)) # Defining the position of the text
    snail_x_position -=0.5 # Creating the animation on the snail sprite
    screen.blit(snail_surface,(snail_x_position,250)) # Creating the 
    if snail_x_position <= -100:snail_x_position = 800
    pygame.display.update() # Updating window
    clock.tick(200) # limiting framerate to 120fps
