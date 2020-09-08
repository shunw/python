import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

display_width = 800
display_height = 600

pygame.init()
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True
    while intro: 
        for event in pygame.event.get():
            # print (event)
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        
        # added
        pygame.draw.rect(gameDisplay, red, (display_width/2 - 5.5*60, display_height/2 - 60, 60*11, 2*60))
        
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('A bit Racey', largeText)
        TextRect.center = (display_width/2, display_height/2)
        
        gameDisplay.blit(TextSurf, TextRect)
        
        # added
        b = pygame.display.blit()

        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit()