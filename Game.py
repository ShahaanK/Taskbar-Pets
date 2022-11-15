import pygame

if __name__ == "__main__":
    pygame.init()

    size = (800, 600)
    screen = pygame.display.set_mode(size)  # Sets the size of our screen.
    pygame.display.set_caption("Taskbar Pets")
    done = False # Loop until the user clicks the close button.

    # --- Main Program loop
    while not done:
        # ---- Main event loop.
        for event in pygame.event.get(): # User does something.
            if event.type == pygame.QUIT: # If they click close.
                done = True; # Change the flag so we are done

        screen.fill(0)  # Background color.
        pygame.draw.rect(screen, (0, 111, 111), (50,50,100,100), 0)


        pygame.display.flip() # Updates the game screen so keep on bottom.
