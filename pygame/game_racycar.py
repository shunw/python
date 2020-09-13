import pygame
import time
import random


pygame.init()

display_width = 800
display_height = 600

#======= added
button_lt_x = display_width/2 - 5.5*60
button_lt_y = display_height/2 - 60
button_width = 60*11
button_height = 2*60
button_rb_x = button_lt_x + button_width
button_rb_y = button_lt_y + button_height

#======= added end

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)

block_color = (53, 115, 255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')

def things_dodged(count): 
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: {}'.format(count), True, black)
    gameDisplay.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    # game_loop()

def crash():
    message_display('You Crashed')

def button(msg, mx, my, w, h, ic, ac, action = None): 
    '''
    statechange: flag to change the state or not
    '''
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print (click)

    if mx + w > mouse[0] > mx and my + h > mouse[1] > my: 
        pygame.draw.rect(gameDisplay, ac, (mx, my, w, h))

        if click[0] == 1 and action != None: 
            action()
            
    else: 
        pygame.draw.rect(gameDisplay, ic, (mx, my, w, h))
    
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    # smallText = pygame.font.SysFont('comicsansms', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((mx + (w/2)), (my + (h/2)))
    gameDisplay.blit(textSurf, textRect)


import enum
class GameState(enum.Enum):
    Quit = -1
    Intro = 0
    Start = 1
    Running = 2
    Crash = 3
    

class racycar(): 
    def __init__(self): 
        self.state = GameState.Intro
        self.x = (display_width * .45)
        self.y = (display_height * .8)
        
        self.x_change = 0
        self.y_change = 0

        self.thing_startx = random.randrange(0, display_width)
        self.thing_starty = -600
        self.thing_speed = 7
        self.thing_width = 100
        self.thing_height = 100

        self.thingCount = 1
        self.dodged = 0
        self.score = 0
        
        self.gameExit = False

    def reset(self): 
        self.state = GameState.Intro
        self.x = (display_width * .45)
        self.y = (display_height * .8)
        
        self.x_change = 0
        self.y_change = 0

        self.thing_startx = random.randrange(0, display_width)
        self.thing_starty = -600
        self.thing_speed = 7
        self.thing_width = 100
        self.thing_height = 100

        self.thingCount = 1
        self.dodged = 0
        
        self.gameExit = False

    def intro(self): 
        '''
        purpose is to show the start button and after people click the button the game state will change to game running (into the game loop)
        '''
        gameDisplay.fill(white)

        
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        # largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('A bit Racey', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        # pygame.draw.rect(gameDisplay, green, (button_lt_x, button_lt_y, button_width, button_height))
        mouse = pygame.mouse.get_pos()
        # pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
        # pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
        
        # if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
        #     pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
        # else: 
        #     pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
        
        # smallText = pygame.font.Font('freesansbold.ttf', 20)
        # textSurf, textRect = text_objects('GO!', smallText)
        # textRect.center = ((150 + (100/2)), (450 + (50/2)))
        # gameDisplay.blit(textSurf, textRect)

        # pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        button('GO!', 150, 450, 100, 50, green, bright_green, self.game_run)
        button('Quit!', 550, 450, 100, 50, red, bright_red)

        for event in pygame.event.get():
            # print (event)
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                px, py = event.pos
                if (px in range(int(button_lt_x),int(button_rb_x))) and (py in range(int(button_lt_y),int(button_rb_y))):
            
                    self.state = GameState.Running
                    # print ('started')
                    return 

    def game_run(self):
        '''
        purpose: 
            game loop --- control the race car move, left and right; 
            when it hits something, it will show crashed and then change the game state to intro.
            and reset all the paramter to the initial status
        '''
        self.state = GameState.Running
        for event in pygame.event.get():
            
            if event.type == pygame. QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_change = -5
                if event.key == pygame.K_RIGHT:
                    self.x_change = 5
                if event.key == pygame.K_UP:
                    self.y_change = -5
                if event.key == pygame.K_DOWN:
                    self.y_change = 5
                    
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.y_change = 0
            
        self.x += self.x_change
        self.y += self.y_change
        

        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(self.thing_startx, self.thing_starty, self.thing_width, self.thing_height, black)
        self.thing_starty += self.thing_speed

        car(self.x, self.y)
        things_dodged(self.dodged)

        if self.x > display_width - car_width or self.x < 0: 
            self.state = GameState.Intro
            # print ('im crashed1')
            crash()
            self.reset()
            
        
        # when the obj is passed through the window, need to restart the obj
        if self.thing_starty > display_height: 
            self.thing_starty = 0 - self.thing_height
            self.thing_startx = random.randrange(0, display_width)
            self.dodged += 1
            self.thing_speed += 1
            self.thing_width += (self.dodged * 1.2)
        
        if self.y < self.thing_starty + self.thing_height:
            # print ('y crossover')
            self.score += 1
        
            if self.x > self.thing_startx and self.x < self.thing_startx + self.thing_width or self.x+car_width > self.thing_startx and self.x + car_width < self.thing_startx + self.thing_width:
                # print ('x crossover')
                self.state = GameState.Intro
                # print ('im crashed2', self.state)
                crash()
                self.reset()
                        

    def game_loop(self): 
        '''
        purpose: 
            is to link the intro and the game loop by check the game status
            if status is intro, it will show the button
            if status is running, it will run the game till crash. 
        '''
        while True:
            # print (self.state)
            if self.state == GameState.Intro:
                self.intro()
            elif self.state == GameState.Running:
                self.game_run()
            pygame.display.update()
            clock.tick(15)
        

race = racycar()    
race.game_loop()

pygame.quit()
quit()
