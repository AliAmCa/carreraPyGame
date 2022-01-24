import pygame
import sys


class Game():
    
    corredores = []
    __startLine= 20
    __finishLine= 620
    
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640,480))
        self.__screen.fill((246,147,48))
        pygame.display.set_caption("Carrera de bichos")
        self.__background = pygame.image.load("imagenes/back.jpg")
        
        self.runner = pygame.image.load("imagenes/ball.png")
        
    def competir(self):
        gameOver= False
        while not gameOver:
            #Comprobacion de los eventos
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    gameOver=True
                    
                    
            # Renderizar la pantalla      
            self.__screen.blit(self.__background,(0,0))
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()
                    

if __name__ =='__main__':
    pygame.font.init()
    game = Game()
    
        