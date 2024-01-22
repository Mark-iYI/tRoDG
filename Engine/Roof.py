import pygame
import os


class Roof:
    def __init__(self, rect: tuple[int, int, int, int], source, classes):
        self.rect = pygame.Rect(*rect)
        self.texture_name = os.path.split(source)[-1]
        self.texture = pygame.image.load(source)
        self.alpha = 255
        self.classes = []

    def split_alpha(self, value: int):
        self.alpha += value
        if self.alpha < 0:
            self.alpha = 0
        elif self.alpha > 255:
            self.alpha = 255
        self.texture.set_alpha(self.alpha)

    def get_data(self):
        return (
            self.rect,
            self.texture_name,
            self.classes
        )
