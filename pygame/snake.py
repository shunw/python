'''
this game is for memory of the eating snake in nokia, classic game
'''

import pygame
import enum

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
green = (0, 200, 0)

class GameState(enum.Enum):
    Intro = 0
    Running = 1
    Eaten = 2
    Crash = 3
    Pause = 4

def pygame_quit():
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            quit()

class Game_Snake():
    def __init__(self):
        pass

    def _snake_shape(self): 
        pass
    def game_loop(self):
        '''
        this is loop all the process for the game snake
        '''
        pygame.init()
        gameDisplay = pygame.display.set_mode((800, 600))
        gameDisplay.fill(black)

        while True:
            
            pygame_quit()

            pixAr = pygame.PixelArray(gameDisplay)
            pixAr[10:20, 10:20] = green
            # pixAr[11][20] = green

            pygame.display.update()


        


if __name__ == '__main__':
    snake = Game_Snake()
    snake.game_loop()