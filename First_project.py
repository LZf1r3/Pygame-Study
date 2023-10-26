import pygame  # Importing the python gaming library
from sys import exit  # Import exit from the system library

pygame.init()  # Initializing pygame
# Defining the size of the screen/window
screen = pygame.display.set_mode((800, 400))
# Defining the name on the window
pygame.display.set_caption("LZ's First Game")
clock = pygame.time.Clock()  # Creating an object for frameratelimit
# pygame.font.Font(font type, font size )
test_font = pygame.font.Font(
    'UltimatePygameIntro-main/font/Pixeltype.ttf', 50)
# Importing snail image <convert_alpha means that when converting the image to a easier picture it will keep the original values such as png
snail_surface = pygame.image.load(
    'UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(700, 300))

# Importing sky picture for background
sky_surface = pygame.image.load(
    'UltimatePygameIntro-main/graphics/Sky.png').convert()

# Importing ground picture for the ground
ground_surface = pygame.image.load(
    'UltimatePygameIntro-main/graphics/ground.png').convert()

# teste_font.render(text, AA, color) <AA means anti-aliasing, which is to smooth the edges of the text>
score_surface = test_font.render("My Game", False, "Black")
score_rectangle = score_surface.get_rect(center=(400,50))
player_surface = pygame.image.load(
    "UltimatePygameIntro-main/graphics/player/player_walk_1.png").convert_alpha()
# player_surface.ger_rect(topleft = (x,y))
player_rectangle = player_surface.get_rect(midbottom=(80, 300))

while True:  # Loop to keep the window's appearance
    for event in pygame.event.get():  # Loop for checking input from the user in case they want to quit the game
        if event.type == pygame.QUIT:  # Checking event
            pygame.quit()  # Quiting pygame
            exit()  # Ending every functioning code
    #    if event.type == pygame.MOUSEMOTION:
    #        print(event.pos)
    #    if event.type == pygame.MOUSEBUTTONDOWN:
    #        print("mouse down")
    #    if event.type == pygame.MOUSEBUTTONUP:
    #        print("mouse up")
    # Screen.blit(surface escolhida, (posicao))
        if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos):
                exit()
    screen.blit(sky_surface, (0, 0))
    # Defining the position of the ground
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen,'pink',score_rectangle)
    pygame.draw.rect(screen,'pink',score_rectangle,10)
    dacing = pygame.draw.line(screen,"pink",(0,0),pygame.mouse.get_pos(),10)
    if snail_rectangle.collidepoint(dacing):
        screen.blit(snail_surface,(600,200))
    screen.blit(score_surface, score_rectangle)  # Defining the position of the text

    snail_rectangle.x -= 1
    if snail_rectangle.x <= -100:
        snail_rectangle.x = 800
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)
    if snail_rectangle.colliderect(player_rectangle):print("Dead"),exit()
   
    # if player_rectangle.colliderect(snail_rectangle):
    #    print("Collision")

    # mouse_position = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint((mouse_position)):
    #    print(pygame.mouse.get_pressed())

    pygame.display.update()  # Updating window
    clock.tick(120)  # limiting framerate to 120fps
