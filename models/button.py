from config import *

class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#fc9803',
            'hover': '#995c02',
            'pressed': '#693f01',
        }
        
        font = pygame.font.SysFont('Arial', 40)
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
                
        self.buttonSurface.blit(self.buttonSurf, [self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2, self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])
        self.screen.blit(self.buttonSurface, self.buttonRect)
    
    @staticmethod    
    def myFunction():
        print('Button Pressed')