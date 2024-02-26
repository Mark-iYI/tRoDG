import math
import os

import pygame
from . import consts


class Player:
    def __init__(self, rect: tuple[int, int, int, int], texture: os.PathLike, speed: int, step_timer: int, inventory):
        self.texture = texture
        self.speed = speed
        self.rect = pygame.Rect(*rect)
        self.step_counter = 0
        self.step_timer = step_timer
        self.moving = False
        self.move_directions = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        self.inventory = inventory

    def move(self, maps):
        ...
        # move_directions = []
        # for key, value in self.move_directions.items():
        #     if value:
        #         move_directions.append(consts.MOVEMENT_KEYS[key])
        # x, y = 0, 0
        # for direction in move_directions:
        #     dx, dy = direction
        #     x += dx
        #     y += dy
        # if x != 0 or y != 0:
        #     angle = math.degrees(math.atan2(y, x))
        #     if angle < 0:
        #         angle += 360
        #     radian = math.radians(angle)
        #     y = math.sin(radian) * self.speed
        #     x = math.cos(radian) * self.speed

        # new_rect = self.rect.copy()
        # new_rect.x += x
        # for wall in maps.walls + maps.doors:
        #     if new_rect.colliderect(wall.rect):
        #         # Проверяем по оси X
        #         if new_rect.move(x, 0).colliderect(wall.rect):
        #             new_rect.x -= x  # Возвращаем игрока назад по оси X
        #
        # new_rect.y += y
        # for wall in maps.walls + maps.doors:
        #     if new_rect.colliderect(wall.rect):
        #         # Проверяем по оси Y
        #         if new_rect.move(y, 0).colliderect(wall.rect):
        #             new_rect.y -= y  # Возвращаем игрока назад по оси y
        # self.rect = new_rect  # Обновляем позицию игрока


        # Обрапотка поверхностей
        # for surface in maps.surfaces:
        #     if self.rect.colliderect(surface.rect):
        #         self.step_counter += 1
        #         if self.step_counter >= self.step_timer:
        #             self.step_counter = 0
        #             surface.get_step().play(self, [self.rect.x, self.rect.y])

    def get_data(self):
        return [
            (self.rect.x, self.rect.y, self.rect.width, self.rect.height),
            self.texture,
            self.speed,
            self.step_timer,
            self.inventory
        ]