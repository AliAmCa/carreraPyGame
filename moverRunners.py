import sys, random
import pygame
from pygame.locals import *

class Runner():
    __customes= ('turtle','fish','prawn','moray', 'octopus')
    
    def __init__(self, x=0,y=0, custome=None):
        
        ixCustome= random.randint(0,4)
        imagen=pygame.image.load("imagenes/{}.png".format(self.__customes[ixCustome]))
        self.custome= pygame.transform.scale(imagen, (60,60))
        self.position =[x,y]
        self.name= ""

   
        

class Game():
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640,480))
        #self.__screen.fill((246,147,48))
        pygame.display.set_caption("Carrera de bichos")
        imagen=pygame.image.load("imagenes/back3.png")
        self.__background = pygame.transform.scale(imagen, (640,480))
        
        self.runner = Runner(320,240)
        
    def start(self):
        gameOver = False
        
        while not gameOver:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    gameOver=True
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        # Mover runner hacia arriba
                        
                        self.runner.position[1]+=-5
                        
                    elif event.key == K_DOWN:
                        # Mover runner hacia abajo
                         self.runner.position[1]+=5
                    
                    elif event.key == K_RIGHT:
                        # Mover runner hacia dcha
                         self.runner.position[0]+=5
                    
                    elif event.key == K_LEFT:
                        # Mover runner hacia izqda
                         self.runner.position[0]+=-5
                    
                    else:
                        pass
               
            #self.__screen.blit(self.__background,(0,0))     
            self.__screen.blit(self.runner.custome, self.runner.position)
            pygame.display.flip()
                        
                        
                    
                    
                    
                    
                    
                   

if __name__ =='__main__':
    pygame.font.init()
    game = Game()
    game.start()
                           
                    
                    
                    
                    