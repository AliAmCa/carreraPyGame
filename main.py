import pygame
import sys, random


class Runner():
    __customes= ('turtle','fish','prawn','moray', 'octopus')
    
    def __init__(self, x=0,y=0, custome=None):
        
        ixCustome= random.randint(0,4)
        imagen=pygame.image.load("imagenes/{}.png".format(self.__customes[ixCustome]))
        self.custome= pygame.transform.scale(imagen, (60,60))
        self.position =[x,y]
        self.name= "Tortuga"

    def avanzar(self):
        self.position[0]+= random.randint(1,6)
        

class Game():
    
    runners = []
    __posY=(120,200,280,360)
    __names=('Speedy', 'Lentorra', 'Casimira', 'Titi')
    __startLine= 20
    __finishLine= 620
    
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640,480))
        #self.__screen.fill((246,147,48))
        pygame.display.set_caption("Carrera de bichos")
        imagen=pygame.image.load("imagenes/back3.png")
        self.__background = pygame.transform.scale(imagen, (640,480))
        
        for i in range(4):
        
            theRunner=Runner(self.__startLine,self.__posY[i])
            theRunner.name= self.__names[i]
            self.runners.append(theRunner)
        
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver= False
        while not gameOver:
            #Comprobacion de los eventos
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    gameOver=True
                    
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0]>= self.__finishLine:
                    print("{} ha ganado".format(runner.name))
                    gameOver=True
                
            # Renderizar la pantalla      
            self.__screen.blit(self.__background,(0,0))
           
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    self.close()
        
                    

if __name__ =='__main__':
    pygame.font.init()
    game = Game()
    game.competir()
        