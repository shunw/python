'''
this game is for memory of the eating snake in nokia, classic game
'''

import pygame
import enum

black = (0, 0, 0)
white = (255, 255, 255)
bright_green = (0, 255, 0)
green = (0, 200, 0)

display_width = 800
display_height = 600

snake_one_block = 10 # this means after the snake eat one bean, it will have increment 5*5 pixel at its bottom
snake_inital_len = 5*snake_one_block
pixel_width = 1

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
        self.start_x = 0
        self.start_y = 0

    def _snake_shape(self): 
        pass
    def game_loop(self):
        '''
        this is loop all the process for the game snake
        '''
        pygame.init()
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        gameDisplay.fill(black)

        while True:
            
            pygame_quit()

            pixAr = pygame.PixelArray(gameDisplay)
            
            # head
            pixAr[self.start_x:self.start_x + pixel_width, self.start_y + snake_inital_len - snake_one_block : self.start_y + snake_inital_len] = green
            pixAr[self.start_x + snake_one_block - pixel_width :self.start_x + snake_one_block, self.start_y + snake_inital_len - snake_one_block : self.start_y + snake_inital_len] = green
            pixAr[self.start_x :self.start_x + snake_one_block,  self.start_y + snake_inital_len - pixel_width: self.start_y + snake_inital_len] = green

            # body
            pixAr[self.start_x:self.start_x + snake_one_block, self.start_y :self.start_y + snake_inital_len - snake_one_block] = green

            pygame.display.update()


        


if __name__ == '__main__':
    snake = Game_Snake()
    snake.game_loop()