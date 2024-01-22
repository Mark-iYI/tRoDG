import os

import pygame
from .Sound import Sound


class Door:
    def __init__(self, rect, hinge_side, negative_opening, texture_path, sound, classes, lock_value=None):
        self.rect = pygame.Rect(*rect)
        self.negative_opening = negative_opening
        self.hinge_side = hinge_side.strip().lower()

        self.texture_path = texture_path
        self.texture_name = os.path.split(self.texture_path)[-1]

        self.sound_path = sound
        self.sound_name = os.path.split(self.sound_path)[-1]
        sounds = os.listdir(sound)
        self.open_sound = Sound(os.path.join(sound, sounds[0]), False)
        self.close_sound = Sound(os.path.join(sound, sounds[1]), False)

        self.lock_value = lock_value
        self.is_open = False

        # Загружаем текстуру (изображение) двери
        self.texture = pygame.image.load(texture_path)
        self.original_texture = self.texture.copy()

        self.classes = classes

    def interact(self, player):
        permission = True
        if self.lock_value is not None:
            permission = False
            for key in player.inventory["keys"]:
                if key == self.lock_value:
                    permission = True

        if (not self.is_open) and permission:
            angle = 0
            # Получаем текущие координаты прямоугольника двери
            # Определяем, какую сторону нужно сместить для открытия
            if self.hinge_side == 'left':
                self.rect.width, self.rect.height = self.rect.height, self.rect.width
                angle = 90
            if self.hinge_side == 'right':
                self.rect.x += self.rect.width - self.rect.height
                self.rect.width, self.rect.height = self.rect.height, self.rect.width

                angle = -90
            if self.negative_opening:
                self.rect.y -= self.rect.height
                angle = -90

            # Поворачиваем текстуру на 90 градусов
            self.texture = pygame.transform.rotate(self.original_texture, angle)
            self.open_sound.play(player, (self.rect.x, self.rect.y))

            # Устанавливаем флаг открытия
            self.is_open = True

        elif self.is_open and permission:
            if self.negative_opening:
                self.rect.y += self.rect.height
            if self.hinge_side == 'left':
                self.rect.width, self.rect.height = self.rect.height, self.rect.width
            if self.hinge_side == 'right':
                self.rect.width, self.rect.height = self.rect.height, self.rect.width
                self.rect.x -= self.rect.width - self.rect.height
            self.texture = self.original_texture
            self.close_sound.play(player, (self.rect.x, self.rect.y))
            self.is_open = False

    def get_data(self):
        return (
            self.rect,
            self.hinge_side,
            self.negative_opening,
            self.texture_name,
            self.sound_name,
            self.classes,
            self.lock_value
        )
