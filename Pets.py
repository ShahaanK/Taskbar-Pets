import pygame


class Pets():

    def __init__(self, x, y, img):
        self.xPos = x;
        self.yPos = y;
        self.imgOfPet = img;
        self.hunger = 100; # Hunger meter.
        self.state = True; # Alive or dead.
        self.age = 0; # Age of pet.

    def draw(self, screen):
        screen.blit(self.imgOfPet, (self.xPos, self.yPos))

