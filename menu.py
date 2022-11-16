import pygame
import sys

# initializing the constructor
pygame.init()

# screen resolution
res = (800, 600)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (204, 153, 255)

# dark shade of the button
color_dark = (102, 102, 153)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
options_text = smallfont.render('Options', True, color)
play_text = smallfont.render('Play', True, color)
text = smallfont.render('Quit', True, color)

# fills the screen with a color
screen.fill((255, 255, 255))

# Logo image
logoImage = pygame.image.load("Pics/mypets.JPG")
logoImage.set_colorkey((255, 255, 255))
# Using blit to copy content from one surface to other
screen.blit(logoImage, (width / 4, 50))


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 - 50 <= mouse[0] <= width / 2 and (height / 4*3) <= mouse[1] <= (height / 4*3 + 30):
                pygame.quit()
            elif width / 2 <= mouse[0] <= width / 2 + 200 and height / 2 <= mouse[1] <= height / 2 + 100:
                pass # Fixme: Go to play game


    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()


    # if mouse is hovered on a button it
    # changes to lighter shade
    # if half the screen is less than the mouse x position, less than width/2+140 of the screen
    # and
    # screen height / 2 is less than the mouse y position, less than screen height/2+40

    # For the play button
    if width / 2 - 80 <= mouse[0] <= width / 2 + 140 and (height / 4*3 - 100) <= mouse[1] <= (height / 4*3 - 60):
        pygame.draw.rect(screen, color_light, [width / 2 - 80, (height / 4*3 - 100), 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2 - 80, (height / 4*3 - 100), 140, 40])

    # superimposing the text onto our button - Play button
    screen.blit(play_text, (width / 2 - 50, height / 4*3 - 100))


    # For the Options button
    if width / 2 - 80 <= mouse[0] <= width / 2 + 140 and (height / 4*3 - 50) <= mouse[1] <= (height / 4*3 + 10):
        pygame.draw.rect(screen, color_light, [width / 2 - 80, (height / 4*3 - 50), 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2 - 80, (height / 4*3 - 50), 140, 40])

    # superimposing the text onto our button - Play button
    screen.blit(options_text, (width / 2 - 65, height / 4*3 - 50))


    # For the Quit button
    if width / 2 - 50 <= mouse[0] <= width / 2 and (height / 4*3) <= mouse[1] <= (height / 4*3 + 30):
        pygame.draw.rect(screen, color_light, [width / 2 - 80, (height / 4*3), 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2 - 80, (height / 4*3), 140, 40])

    # superimposing the text onto our button - Play button
    screen.blit(text, (width / 2 - 50, height / 4*3))


    # updates the frames of the game
    pygame.display.update()