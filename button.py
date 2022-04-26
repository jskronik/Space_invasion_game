import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initialization of button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (50, 50, 50)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Creating a rectangular button and centering it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The message displayed by the button
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Placing the message in the generated image and centering the button text"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)