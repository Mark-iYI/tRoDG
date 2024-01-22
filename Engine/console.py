import logging

import pygame
from Engine.map.Map import Map
from .Sound import Sound

logging.basicConfig(level=logging.INFO, filename="logs\\last.log", filemode="w",
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')


class Console:
    def __init__(self):
        self.history = []
        self.lines = []
        self.pretext = ">>> "
        self.input_text = ""
        self.cursor_pos = 0

    def draw(self, display: pygame.Surface, font: pygame.font.Font):
        inputline = pygame.Surface((display.get_width() - 20, 20))
        inputline.fill((0, 0, 0))
        input_text = self.pretext + self.input_text[:self.cursor_pos] + "|" + self.input_text[self.cursor_pos:]
        input_text = font.render(input_text, True, (255, 255, 255))
        inputline.blit(input_text, (5, 0))
        y_offset = 30
        for line in reversed(self.lines):
            line_surface = font.render(line, True, (255, 255, 255), (100, 100, 100))
            display.blit(line_surface, (10, y_offset))
            y_offset += 20
        display.blit(inputline, (10, 10))

    def handle_backspace(self):
        if self.cursor_pos > 0:
            self.input_text = self.input_text[:self.cursor_pos-1] + self.input_text[self.cursor_pos:]
            self.cursor_pos -= 1

    def handle_return(self, variables: dict):
        self.lines.append(self.pretext + self.input_text)
        self.history.append(self.input_text)
        self.execute_command(self.input_text, variables)
        self.input_text = ""
        self.cursor_pos = 0

    def handle_key_left(self):
        if self.cursor_pos > 0:
            self.cursor_pos -= 1

    def handle_key_right(self):
        if self.cursor_pos < len(self.input_text):
            self.cursor_pos += 1

    def handle_key_default(self, event):
        self.input_text = self.input_text[:self.cursor_pos] + event.unicode + self.input_text[self.cursor_pos:]
        self.cursor_pos += 1

    def event(self, event, variables: dict):
        if event.key == pygame.K_BACKSPACE:
            self.handle_backspace()
        elif event.key == pygame.K_RETURN:
            self.handle_return(variables)
        elif event.key == pygame.K_LEFT:
            self.handle_key_left()
        elif event.key == pygame.K_RIGHT:
            self.handle_key_right()
        else:
            self.handle_key_default(event)

    def log(self, text):
        self.lines.append(text)
        logging.info(text)

    def execute_command(self, text, maps: Map):
        command_with_args = text.strip().split()  # Разделяем введенную строку на слова
        command = command_with_args[0]  # Первое слово - команда
        arguments = command_with_args[1:]  # Остальные слова - аргументы

        # Пример обработки команды move_player
        if command == "tp":
            if len(arguments) >= 2:
                # Первый аргумент - X, второй аргумент - Y
                x = int(arguments[0])
                y = int(arguments[1])

                maps.player.rect.x, maps.player.rect.y = x, y
                self.log("Игрок телепортировался")
            else:
                self.log("Недостаточно аргументов для команды tp")
        elif command == "mksound":
            if len(arguments) >= 2:
                x = int(arguments[1])
                y = int(arguments[2])
                Sound(arguments[0], False).play(maps.player, [x, y])
                self.log("Звук проигран")
            else:
                self.log("Недостаточно аргументов для команды mksound")

        elif command == "map":
            loaded_map = Map.load(arguments[0])
            for k, v in loaded_map.__dict__.items():
                setattr(maps, k, v)

        elif command == "draw_rects":
            maps.draw_rects = not not arguments[0]
