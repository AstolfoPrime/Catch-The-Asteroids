import pygame 
import simpleGE
import random

class Coin (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("asteroid.png")
        self.setSize(50, 50)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
   
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Charlie (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("elon_musk.png")
        self.setSize(100, 70)
        self.position = (320, 445)
        self.move_speed = 10

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.move_speed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.move_speed

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("background_image.png")
       
        #self.coin_sound = simpleGE.Sound("coin.mp3")
        self.number_of_coins = 10
       
        self.charlie = Charlie(self)
        self.coins = []
       
        for self.coin in range(0, self.number_of_coins):
            self.coins.append(Coin(self))
           
        self.sprites = [self.charlie,
                        self.coins]

    def process(self):
        for coin in self.coins:
            if self.charlie.collidesWith(coin):
                coin.reset()
                # self.coin_sound.play()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()