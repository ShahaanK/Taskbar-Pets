import pygame

# Calling the classes.
from Pets import Pets


def keyCheck():
    # If you press space bar the dogs hunger will go up.
    if event.key == pygame.K_SPACE:
        doggo.feed()

    if event.key == pygame.K_p:
        doggo.play()

    if event.key == pygame.K_r:
        doggo.sleep()


if __name__ == "__main__": # Initializer of our game so we load here.
    pygame.init()

    # UI stuff.
    size = (800, 600)
    screen = pygame.display.set_mode(size)  # Sets the size of our screen.
    pygame.display.set_caption("Taskbar Pets")
    myfont = pygame.font.Font('freesansbold.ttf', 30) # Basic font.

    # Setting the images.
    doggoImage = pygame.image.load("Pics/doggo.JPG")

    # Initializing the first pets.
    doggo = Pets(300, 200, doggoImage)

    done = False # Loop until the user clicks the close button. At end.

    # --- Main Program loop
    while not done:
        # ---- Main event loop.
        for event in pygame.event.get(): # User does something.
            if event.type == pygame.QUIT: # If they click close.
                done = True # Change the flag so we are done
            elif event.type == pygame.KEYDOWN: # User preses a key. FIXME: Change later to be mouse button thingy
                keyCheck()

        # Drawing stuff to the screen ------------------------------------------------------
        screen.fill(0)  # Background color.
        pygame.draw.rect(screen, (0, 111, 111), (50, 50, 100, 100), 0)

        doggo.draw(screen) # Uses the method to draw it to screen.

        # Print out the hunger.
        hunger_text = myfont.render("Hunger: " + str(doggo.hunger), 1, (0, 255, 124)) # Setting text.
        screen.blit(hunger_text, (20, 20)) # Printing text to screen.

        # Print out the Health.
        hunger_text = myfont.render("Health: " + str(doggo.health), 1, (0, 255, 124))  # Setting text.
        screen.blit(hunger_text, (40, 40))  # Printing text to screen.

        # Print out the Mood.
        hunger_text = myfont.render("Mood: " + str(doggo.mood), 1, (0, 255, 124))  # Setting text.
        screen.blit(hunger_text, (60, 60))  # Printing text to screen.

        pygame.display.flip() # Updates the game screen so keep on bottom.



