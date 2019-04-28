import pygame, sys

class Juego():
    corredores = []
    __lineaLargada = 20
    __lineaLlegada = 620
    
    def __init__(self):
        self.__pantalla = pygame.display.set_mode((640, 480))
        self.__pantalla.fill((0, 255, 0))
        #self.fondoPantalla = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            self.__pantalla.blit(self.__pantalla, (0,0))
            
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()
    
if __name__ == '__main__':
    juego = Juego()
    pygame.init()
    juego.competir()
    