import pygame


class Pets():

    def __init__(self, x, y, img):
        self.xPos = x
        self.yPos = y
        self.imgOfPet = img
        self.hunger = 100 # Hunger meter.
        self.health = 100 # Health bar.
        self.mood = 100 # Mood bar.
        self.rest = False # If the pet is sleeping.
        self.state = True # Alive or dead.
        self.age = 0 # Age of pet.

    def draw(self, screen):
        screen.blit(self.imgOfPet, (self.xPos, self.yPos))

    def feed(self): # Feed the pet to increase its hunger, mood, health.
        self.hunger += 5
        self.health += 2
        self.mood += 2
        self.maxValues()
        self.death()

    def play(self): # Play with the pet to decrease the hunger and health but increase mood.
        self.hunger -= 3
        self.health -= 5
        self.mood += 5
        self.maxValues()
        self.death()


    def sleep(self): # If the pet sleeps, recover health but decrease hunger and mood.
        self.health += 10
        self.hunger -= 3
        self.mood -= 1
        self.maxValues()
        self.death()


    def death(self):
        # If the pet's health, mood or hunger hits 0, kill the pet.
        if self.health <= 0 or self.mood <= 0 or self.hunger <= 0:
            self.state = False

    def maxValues(self): # Set the max values each pet's health, mood and hunger.
        if self.health >= 100:
            self.health = 100
        if self.mood >= 100:
            self.mood = 100
        if self.hunger >= 100:
            self.hunger = 100