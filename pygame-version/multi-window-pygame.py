import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load("background.png")
        self.background_rect = self.background.get_rect()
        self.DISPLAYSURF = pygame.display.set_mode(self.background.get_size())
        pygame.display.set_caption("Joker")
        self.joke_window = JokeWindow(self.DISPLAYSURF, self.background_rect)
        self.punch_line = PunchLineWindow(self.DISPLAYSURF, self.background_rect)
        current_display = self.joke_window

        while True:
            self.DISPLAYSURF.blit(self.background, self.background_rect)
            current_display.display_stuff()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    current_display.deal_with_click(x, y)
            if current_display.switch_window:
                current_display.switch_window = False
                if current_display == self.joke_window:
                    current_display = self.punch_line
                else:
                    current_display = self.joke_window


class JokeWindow:
    def __init__(self, the_surface, background_rect):
        self.bg_rect = background_rect
        self.surface = the_surface
        self.message_font = pygame.font.SysFont("Arial", 20)
        self.joke_text = "What's the difference between a buffalo and bison?"
        self.okay_btn = pygame.image.load("okay.png")
        self.okay_btn_rect = self.okay_btn.get_rect()
        self.line = self.message_font.render(self.joke_text, 0, (255, 255, 255))
        self.line_rect = self.line.get_rect()
        self.line_rect.centerx = self.bg_rect.centerx
        self.line_rect.y = 100
        self.okay_btn_rect.centerx = self.bg_rect.centerx
        self.okay_btn_rect.y = 150
        self.switch_window = False

    def display_stuff(self):
        self.surface.blit(self.line, self.line_rect)
        self.surface.blit(self.okay_btn, self.okay_btn_rect)

    def deal_with_click(self, x, y):
        if self.okay_btn_rect.collidepoint(x, y):
            self.switch_window = True


class PunchLineWindow:
    def __init__(self, the_surface, background_rect):
        self.bg_rect = background_rect
        self.surface = the_surface
        self.message_font = pygame.font.SysFont("Arial", 20)
        self.punch_line = "You can't wash your hands in a buffalo!"
        self.line = self.message_font.render(self.punch_line, 0, (255, 255, 255))
        self.line_rect = self.line.get_rect()
        self.line_rect.centerx = self.bg_rect.centerx
        self.line_rect.y = 100
        self.okay_btn = pygame.image.load("okay.png")
        self.okay_btn_rect = self.okay_btn.get_rect()
        self.okay_btn_rect.centerx = self.bg_rect.centerx
        self.okay_btn_rect.y = 150
        self.close_btn = pygame.image.load("close.png")
        self.close_btn_rect = self.close_btn.get_rect()
        self.close_btn_rect.centerx = self.bg_rect.centerx
        self.close_btn_rect.y = 210
        self.switch_window = False

    def display_stuff(self):
        self.surface.blit(self.line, self.line_rect)
        self.surface.blit(self.okay_btn, self.okay_btn_rect)
        self.surface.blit(self.close_btn, self.close_btn_rect)

    def deal_with_click(self, x, y):
        if self.okay_btn_rect.collidepoint(x, y):
            self.switch_window = True
        elif self.close_btn_rect.collidepoint(x, y):
            pygame.quit()
            sys.exit()


my_game = Game()
