import time
import pygame
import random

class monster :
    def __init__(self,display):
        self.homebg = pygame.image.load('assets/logo3.png')
        self.shoot = pygame.image.load('assets/shooter.png')
        self.bullet = pygame.image.load('assets/bullet.png')
        self.windoww = 800
        self.windowh = 600
        #self.obj= self.shoot
        self.clock = pygame.time.Clock()
        self.screen = display
        self.car = 10
        # blood
        self.red = (255, 0, 0)
        # back
        self.white = (255, 255, 255)
        # text + bullet
        self.black = (0, 0, 0)

        self.black_comp = (176, 190, 197)

    def monster(self,version, width, height):
        monster = pygame.image.load('assets/mon' + str(version) + '.png')
        self.screen.blit(monster, (width, height))

    def text_objects(self,text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def message_display(self,text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((self.windoww / 2), (self.windowh / 2))
        self.screen.fill(self.red)
        self.screen.blit(TextSurf, TextRect)
        pygame.display.update()

        time.sleep(2)
        #start_game()


    def move(self,x, y):
        self.screen.blit(self.shoot, (x, y))

    def bull(self,x, y):
        while x < 800:
            self.screen.blit(self.bullet, (x, y))
            self.clock.tick(40)
            x += 40

    def score_keeper(self,count):
        li = [0]
        # current score
        font = pygame.font.SysFont(None, 25)
        text = font.render("kills : " + str(count), True, self.black)
        self.screen.blit(text, (0, 0))
        li.append(count)
        # high score

        font = pygame.font.SysFont(None, 25)
        text = font.render("High Score : " + str(max(li)), True, self.black)
        self.screen.blit(text, (400, 0))

    def i_am_dead(self):
        self.message_display('You are Dead')