import pygame


class Pets():

    def __init__(self):
        self.xPos = 0;
        self.yPos = 0;
        self.imgOfPet;
        self.hunger = 100; # Hunger meter.
        self.state = True; # Alive or dead.
        self.age = 0; # Age of pet.

    def draw(self, screen):
        pet1 = pygame.image.load("Pics/doggo.JPG");
        pygame.display.blit(pet1, )