
import pygame
import random
import time
import extras
from pygame.locals import *

#import locale

pygame.init()

windoww = 800
windowh = 600
clock =pygame.time.Clock()


screen = pygame.display.set_mode((windoww,windowh))
pygame.display.set_caption('----Shooter----')

#blood
red = (255, 0, 0)
# back
white=(255, 255, 255)
# text + bullet
black= (0, 0, 0)

black_comp = (176,190,197)

def start_game():
    exit = False
    # dependency over image dimensions
    shooter_x = -30
    shooter_y = 200
    shooter_change = 0
    count,kill,prevh,prew=0,0,0,0

    # monster
    monster_version = random.randrange(1,5)
    monster_width = random.randrange(200, 780)
    monster_height = random.randrange(0, 550)

    while not exit :
        shot=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                print(" exit triggered ")
                pygame.quit()
                quit()
            if shooter_y <= (422) and shooter_y >= 0:
                if event.type == pygame.MOUSEBUTTONDOWN :
                    # check border dimensions
                    if event.button == 1:
                        shot=1
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_UP:
                        shooter_change = -50
                    if event.key == pygame.K_DOWN :
                        shooter_change = 50
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_DOWN or event.type == pygame.K_UP :
                        shooter_change =0
            else:
                # push middle
                shooter_y = 200
                print(" boundry triggered ")


        screen.fill(black_comp)
        #background home : screen.blit(homebg, (-30,350))


        #change pos
        shooter_y+=shooter_change
        shooter_change = 0
        if shot :
            extras.monster(screen).bull(179, shooter_y+67)

        # triger monster
        extras.monster(screen).monster(monster_version,monster_width,monster_height)
        if count==50 :
            count=0
            monster_version = random.randrange(1, 5)
            monster_width = random.randrange(0, 680)
            monster_height = random.randrange(0, 480)

        # dyanmic shooter display
        extras.monster(screen).move(shooter_x,shooter_y)
        clock.tick(40)
        count+=1
        # issue here
        #time.sleep(5)

        if monster_height<= (shooter_y+67) <=(monster_height+100) and shot == 1:
            if monster_width != prew and monster_height != prevh :
                kill += 1
            prevh = monster_height
            prew =monster_width


        # dead screen
        if (shooter_x+10)<=monster_width<=(shooter_x+120) and monster_height>=(shooter_y+40) and (monster_height)<=(shooter_y+140):
            time.sleep(1)
            extras.monster(screen).message_display("Your Score : "+ str(kill))
            start_game()

        extras.monster(screen).score_keeper(kill)
        pygame.display.update()

if __name__ == "__main__":
    start_game()
    pygame.quit()