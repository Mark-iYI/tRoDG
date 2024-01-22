import os
import random

from .Sound import Sound
import pygame


class Surface:
    def __init__(self, rect: tuple[int, int, int, int], sound: os.PathLike, classes):
        self.rect = pygame.Rect(*rect)
        self.sound_path = sound
        self.sound_type = os.path.split(sound)[-1]
        self.sounds = []
        for i in os.listdir(sound):
            self.sounds.append(Sound(os.path.join(sound, i), False))
        self.classes = classes

    def get_step(self):
        return self.sounds[random.randint(0, 4)]

    def get_data(self):
        return (
            self.rect,
            self.sound_type,
            self.classes
        )
