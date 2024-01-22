import pygame
import os


class Sound:
    def __init__(self, source: os.PathLike, loop: bool):
        self.source = source
        self.name = os.path.split(source)[-1]
        self.sound = pygame.mixer.Sound(os.path.join(source))
        self.loop = loop

    def play(self, player, position):
        distance = pygame.math.Vector2(player.rect.center).distance_to(position)
        max_distance = 1920  # Максимальное расстояние для звука (можно изменить)

        if distance > max_distance:
            volume = 0  # Если игрок слишком далеко, звук выключен
        else:
            volume = 1 - (distance / max_distance)  # Рассчитываем громкость по расстоянию
        self.sound.set_volume(volume)
        self.sound.play(self.loop)
        print("play")

    def get_data(self):
        return [
            self.source,
            self.loop
        ]
