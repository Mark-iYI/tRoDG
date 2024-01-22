import os
from Engine.Wall import Wall
from Engine.Sound import Sound
from Engine.Surface import Surface
from Engine.Roof import Roof
from Engine.Door import Door


def load_walls(data):
    walls = []
    for wall in data:
        walls.append(
            Wall(wall[0], wall[1])
        )
    return walls


def load_sounds(data, map_name):
    sounds = []
    for sound in data:
        sounds.append(
            Sound(
                os.path.join("data\\Maps\\", map_name, "assets\\sounds\\", sound[0]), sound[1]
            )
        )
    return sounds


def load_surfaces(data, map_name):
    surfaces = []
    for surface in data:
        surfaces.append(
            Surface(
                surface[0], os.path.join("data\\Maps\\", map_name, "assets\\sounds\\steps", surface[1]), surface[2]
            )
        )
    return surfaces


def load_roofs(data, map_name):
    roofs = []
    for roof in data:
        roofs.append(
            Roof(
                roof[0], os.path.join("data\\Maps\\", map_name, "assets\\textures\\roofs", roof[1]), roof[2]
            )
        )
    return roofs


def load_doors(data, map_name):
    doors = []
    for door in data:
        doors.append(
            Door(
                door[0], door[1], door[2],
                os.path.join("data\\Maps\\", map_name, "assets\\textures\\doors", door[3]),
                os.path.join("data\\Maps\\", map_name, "assets\\sounds\\doors", door[4]),
                door[5],
                door[6]
            )
        )
    return doors
