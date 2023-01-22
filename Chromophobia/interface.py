import pygame as pg


class Interface:

    def __init__(self, screen, x, y, height, width, color, GUI_alpha, BG_alpha):
        self.screen = screen
        self.x, self.y = x, y
        self.width, self.height = height, width
        self.color = color
        self.running = True
        self.GUI_alpha, self.BG_alpha = GUI_alpha, BG_alpha

        self.Background = pg.Surface(self.screen.get_size())
        self.GUI = pg.Surface((self.width, self.height))
        self.GUI_rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.clock = pg.time.Clock()

    def Darken_Background(self):
        self.Background.set_alpha(self.BG_alpha)
        self.Background.fill((15, 15, 15))
        self.screen.blit(self.Background, (0, 0))
        return

    def ShowGUI(self):
        self.GUI.set_alpha(self.GUI_alpha)
        self.GUI.fill(self.color)
        self.screen.blit(self.GUI, (self.x, self.y))
        return

    def Display(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

            pg.display.flip()
            self.clock.tick(60)
        return
