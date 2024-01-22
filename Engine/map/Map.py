import pickle
import pygame
from Engine.map.import_functions import *
from Engine.Player import Player
from ..consts import *


class Map:
    def __init__(self, name, player_data, walls_data, sounds_data, surfaces_data, roofs_data, doors_data):
        self.name = name
        self.player = Player(*player_data)
        self.walls = load_walls(walls_data)
        self.sounds = load_sounds(sounds_data, self.name)
        self.surfaces = load_surfaces(surfaces_data, self.name)
        self.roofs = load_roofs(roofs_data, self.name)
        self.doors = load_doors(doors_data, self.name)
        self.texture = self.load_texture()
        self.draw_rects = False
        self.surface = pygame.Surface((self.texture.get_width(), self.texture.get_height()))
        self.pos = [0, 0]
        self.params = self.update_params()
        self.save()

    def load_texture(self):
        texture_path = os.path.join("data", "Maps", self.name, "texture.png")
        try:
            return pygame.image.load(texture_path)
        except pygame.error:
            return None

    def update_params(self):
        params = {
            "name": self.name,
            "player": self.player.get_data(),
            "walls": [wall.get_data() for wall in self.walls],
            "surfaces": [surface.get_data() for surface in self.surfaces],
            "sounds": [sound.get_data() for sound in self.sounds],
            "roofs": [roof.get_data() for roof in self.roofs],
            "doors": [door.get_data() for door in self.doors]
        }
        return params

    def auto_move_map(self, display):
        self.pos[0] =\
            display.get_width() / 2 - self.player.rect.centerx - \
            (pygame.mouse.get_pos()[0] - display.get_width() / 2) * 0.5
        self.pos[1] =\
            display.get_height() / 2 - self.player.rect.centery - \
            (pygame.mouse.get_pos()[1] - display.get_height() / 2) * 0.5

    def draw(self, display):
        self.surface.blit(self.texture, (0, 0))

        for roof in self.roofs:
            alpha_change = -20 if self.player.rect.colliderect(roof.rect) else 20
            roof.split_alpha(alpha_change)
            self.surface.blit(roof.texture, roof.rect)
        for door in self.doors:
            self.surface.blit(door.texture, door.rect)

        if self.draw_rects:
            for wall in self.walls:
                pygame.draw.rect(self.surface, COLORS["red"], wall.rect)
            for surface in self.surfaces:
                pygame.draw.rect(self.surface, COLORS["green"], surface.rect)
            for roof in self.roofs:
                color = COLORS["blue"]
                pygame.draw.rect(self.surface, color, roof.rect)
            for door in self.doors:
                color = COLORS["yellow"]
                pygame.draw.rect(self.surface, color, door.rect)
            pygame.draw.rect(self.surface, (0, 0, 0), self.player.rect)

        self.pos[0] =\
            display.get_width() / 2 - self.player.rect.centerx - \
            (pygame.mouse.get_pos()[0] - display.get_width() / 2) * 0.5
        self.pos[1] =\
            display.get_height() / 2 - self.player.rect.centery - \
            (pygame.mouse.get_pos()[1] - display.get_height() / 2) * 0.5
        display.blit(self.surface, self.pos)

    def save(self):
        self.update_params()
        path = os.path.join("data", "Maps", self.name, "params.pkl")
        os.makedirs(os.path.join("data", "Maps", self.name, "assets", "sounds", "steps"), exist_ok=True)
        os.makedirs(os.path.join("data", "Maps", self.name, "assets", "sounds", "doors"), exist_ok=True)
        os.makedirs(os.path.join("data", "Maps", self.name, "assets", "textures", "roofs"), exist_ok=True)
        os.makedirs(os.path.join("data", "Maps", self.name, "assets", "textures", "doors"), exist_ok=True)
        with open(path, 'wb') as file:
            pickle.dump(self.params, file)

    @staticmethod
    def load(filename):
        path = os.path.join("data", "Maps", filename, "params.pkl")
        with open(path, 'rb') as file:
            data = pickle.load(file)
        return Map(data["name"],
                   data["player"],
                   data["walls"],
                   data["sounds"],
                   data["surfaces"],
                   data["roofs"],
                   data["doors"])
