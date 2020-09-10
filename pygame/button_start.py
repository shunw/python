import pygame
import game_racycar
# link: http://cncc.bingj.com/cache.aspx?q=pygame%2c+click+mouse&d=4506842382995224&mkt=en-US&setlang=en-US&w=53morcbqkKQBedjNi4eBUjX3xN6ZcWs9

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

display_width = 800
display_height = 600

button_lt_x = display_width/2 - 5.5*60
button_lt_y = display_height/2 - 60
button_width = 60*11
button_height = 2*60
button_rb_x = button_lt_x + button_width
button_rb_y = button_lt_y + button_height

pygame.init()
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True
    while intro: 
        
        gameDisplay.fill(white)
        
        # added
        pygame.draw.rect(gameDisplay, red, (button_lt_x, button_lt_y, button_width, button_height))
        
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('A bit Racey', largeText)
        TextRect.center = (display_width/2, display_height/2)
        
        gameDisplay.blit(TextSurf, TextRect)
        
        # added
        # b = pygame.display.blit()
        
        for event in pygame.event.get():
            # print (event)
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                if pos[0] > button_lt_x and pos[0] < button_rb_x and pos[1] > button_lt_y and pos[1] < button_rb_y:

                    game_racycar.game_loop()

        pygame.display.update()
        clock.tick(15)
# print (button_lt_x, button_rb_x)
# print (button_lt_y, button_rb_y)
game_intro()
pygame.quit()
quit()