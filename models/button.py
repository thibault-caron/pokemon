from config import *

class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, screen = None, radius = 10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.radius = radius
        self.text = buttonText

        self.fillColors = {
            'normal': '#fc9803',
            'hover': '#995c02',
            'pressed': '#693f01',
        }
        
        font = pygame.font.Font('assets/pokemon_classic.ttf', 20)
        
        self.screen = screen
        
        # self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        
    def process(self):
        mousePos = pygame.mouse.get_pos()
        
        if self.buttonRect.collidepoint(mousePos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                current_color = self.fillColors["pressed"]
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                current_color = self.fillColors["hover"]
                self.alreadyPressed = False
        else:
            current_color = self.fillColors["normal"]
                
        pygame.draw.rect(self.screen, current_color, self.buttonRect, border_radius = self.radius)
                
        # self.buttonSurface.blit(self.buttonSurf, [self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2, self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])
        self.screen.blit(self.buttonSurf,
            (self.buttonRect.x + (self.buttonRect.width - self.buttonSurf.get_width()) / 2,
             self.buttonRect.y + (self.buttonRect.height - self.buttonSurf.get_height()) / 2)
        )