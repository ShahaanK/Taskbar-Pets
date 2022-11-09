import sys

import pygame

if __name__ == "__main__":
    pygame.init()

    size = (800, 600)
    screen = pygame.display.set_mode(size)  # Sets the size of our screen.
    pygame.display.set_caption("Taskbar Pets")

    # --- Main event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        pygame.draw.rect(screen, (0, 111, 111), (50,50,100,100), 0)
        pygame.display.flip()
