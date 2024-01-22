import pygame


class Wall:
    def __init__(self, rect: tuple[int, int, int, int], classes=None):
        self.rect = pygame.Rect(*rect)
        self.classes = classes

    def get_data(self):
        return (
            self.rect,
            self.classes
        )
