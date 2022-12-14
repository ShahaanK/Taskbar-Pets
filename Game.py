import pygame

# Calling the classes.
from Pets import Pets

# Define some colors.
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define some constants.
MAX_HEALTH = 100

def keyCheck():
    # If you press space bar the dogs hunger will go up.
    if event.key == pygame.K_SPACE:
        doggo.feed()

    if event.key == pygame.K_p:
        doggo.play()

    if event.key == pygame.K_r:
        doggo.sleep()


if __name__ == "__main__":  # Initializer of our game so we load here.
    pygame.init()

    # UI stuff.
    size = (800, 600)
    screen = pygame.display.set_mode(size)  # Sets the size of our screen.
    pygame.display.set_caption("Taskbar Pets")
    myfont = pygame.font.Font('freesansbold.ttf', 30)  # Basic font.

    #ATTEMPT TO MAKE ANIMATIONS THEN MOVE FROM MAIN TO NEW FILE.
    doggoImageArray = pygame.image.load("Pics/DogGifFrames/doggy_1.png"), pygame.image.load("Pics/DogGifFrames/doggy_2.png"), \
                 pygame.image.load("Pics/DogGifFrames/doggy_3.png"), pygame.image.load("Pics/DogGifFrames/doggy_4.png"), \
                     pygame.image.load("Pics/DogGifFrames/doggy_5.png"), pygame.image.load("Pics/DogGifFrames/doggy_6.png")



    clock = pygame.time.Clock()
    animationCounter = 0

    # Setting the images.
    doggoImage = pygame.image.load("Pics/DogGifFrames/doggy_1.png")
    doggoImageWidth = doggoImage.get_width()
    doggoImageHeight = doggoImage.get_height()

    doggoImage = pygame.transform.scale(doggoImage, (doggoImageWidth/2,doggoImageHeight/2))
    doggoImage.set_colorkey((132, 126, 135)) # Removes one of the colors in the background, can't remove both cause this will only work on last color written.

    deadDoggoImage = pygame.image.load("Pics/doggoCute.png")

    # Initializing the first pets.
    doggo = Pets(300, 200, doggoImage)
    doggoDead = Pets(300, 200, deadDoggoImage)

    done = False  # Loop until the user clicks the close button. At end.

    # --- Main Program loop
    while not done:
        # ---- Main event loop.
        for event in pygame.event.get():  # User does something.
            if event.type == pygame.QUIT:  # If they click close.
                done = True  # Change the flag so we are done
            elif event.type == pygame.KEYDOWN:  # User preses a key. FIXME: Change later to be mouse button thingy
                keyCheck()

        # Drawing stuff to the screen ------------------------------------------------------
        screen.fill(0)  # Background color.

        # TEMP ANIMATION STUFF
        clock.tick(60)

        for i in range(6):
            if animationCounter == 0:
                #doggoImageArray[0] = pygame.transform.scale(doggoImageArray[0], (doggoImageArray[0].get_width() / 2, doggoImageArray[0].get_height() / 2))
                doggoImageArray[i].set_colorkey((132, 126, 135))
                screen.blit((doggoImageArray[i]), (0, 0))



        # If the dog is alive then do all this.
        if doggo.state:  # FIXME: Change doggo to an array or array list later so we can accomadte multiple pets.

            #doggo.draw(screen)  # Uses the method to draw it to screen.

            # Print out the hunger.
            hunger_text = myfont.render("Hunger: " + str(doggo.hunger), 3, (0, 255, 124))  # Setting text.
            screen.blit(hunger_text, (60, 500))  # Printing text to screen.
            # Attempt at making a hunger bar.
            # MAX_HEALTH*1.5 to make bar longer, 10 is the thickness of the bar.
            pygame.draw.rect(screen, WHITE, (60, 550, MAX_HEALTH*1.5, 10))
            pygame.draw.rect(screen, BLUE, (60, 550, doggo.hunger*1.5, 10))

            # Print out the Health.
            hunger_text = myfont.render("Health: " + str(doggo.health), 1, (0, 255, 124))  # Setting text.
            screen.blit(hunger_text, (335, 500))  # Printing text to screen.
            # Attempt at making a health bar.
            pygame.draw.rect(screen, WHITE, (335, 550, MAX_HEALTH * 1.5, 10))
            pygame.draw.rect(screen, RED, (335, 550, doggo.health * 1.5, 10))

            # Print out the Mood.
            hunger_text = myfont.render("Mood: " + str(doggo.mood), 1, (0, 255, 124))  # Setting text.
            screen.blit(hunger_text, (610, 500))  # Printing text to screen.
            # Attempt at making a mood bar.
            pygame.draw.rect(screen, WHITE, (610, 550, MAX_HEALTH * 1.5, 10))
            pygame.draw.rect(screen, GREEN, (610, 550, doggo.mood * 1.5, 10))

        else:
            #Print dog dead image.
            doggoDead.draw(screen)

        pygame.display.flip()  # Updates the game screen so keep on bottom.
