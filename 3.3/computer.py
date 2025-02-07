import pygame as pg
from random import randint
from settings import sc


class Computer:

    def __init__(self):
        self.name = 'Компьютер'
        self.stone = pg.transform.scale(pg.image.load('images/r_stone.png'),
                                        (144, 183))
        self.stone_rect = self.stone.get_rect(center=(sc.width - 100,
                                                      sc.height / 2))
        self.scissors = pg.transform.scale(
            pg.image.load('images/r_scissors.png'), (144, 183))
        self.scissors_rect = self.scissors.get_rect(center=(sc.width - 100,
                                                            sc.height / 2))
        self.paper = pg.transform.scale(pg.image.load('images/r_paper.png'),
                                        (144, 183))
        self.paper_rect = self.paper.get_rect(center=(sc.width - 100,
                                                      sc.height / 2))
        self.start = pg.transform.scale(pg.image.load('images/r_start.png'),
                                        (144, 183))
        self.start_rect = self.start.get_rect(center=(sc.width - 100,
                                                      sc.height / 2))
        self.start_rotate = pg.transform.scale(
            pg.image.load('images/r_start.png'), (144, 183))
        self.win = pg.transform.scale(pg.image.load('images/r_win.png'),
                                      (144, 183))
        self.win_rect = self.win.get_rect(center=(sc.width - 100,
                                                  sc.height / 2))
        self.choice = None
        self.rotation = False

    def random_choice(self):
        self.choice = randint(1, 3)

    def blit_image(self, name_image, name_rect):
        sc.win.blit(name_image, name_rect)

    def change_rotation(self, rot):

        if self.rotation == False:
            self.rotation = True
            self.start_rotate = pg.transform.rotate(self.start, rot)
        else:
            self.rotation = False
            self.start_rotate = self.start

    def view_choice(self):
        if self.choice == 1:
            self.blit_image(self.stone, self.stone_rect)
        elif self.choice == 2:
            self.blit_image(self.scissors, self.scissors_rect)
        elif self.choice == 3:
            self.blit_image(self.paper, self.paper_rect)

computer = Computer()
