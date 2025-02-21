from config import *


class Button:
    """ Class to manage buttons action. """
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False,
                 screen=None, radius=10):
        """
        Initialization of the class.
        :param x: Abscissa of the button.
        :param y: Ordinate of the button.
        :param width: Width of the button.
        :param height: Height of the button.
        :param buttonText: Text of the button.
        :param onclickFunction: Set of one click action.
        :param onePress: Set of one press action.
        :param screen: Call of the game screen.
        :param radius: Border radius of the button.
        """
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
        """
        Apply buttons process.
        :return: ∅
        """
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

        pygame.draw.rect(self.screen, current_color, self.buttonRect, border_radius=self.radius)

        self.screen.blit(self.buttonSurf,
                         (self.buttonRect.x + (self.buttonRect.width - self.buttonSurf.get_width()) / 2,
                          self.buttonRect.y + (self.buttonRect.height - self.buttonSurf.get_height()) / 2)
                         )
