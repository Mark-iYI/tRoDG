# здесь подключаются модули
import pygame
import Engine
import math
import pickle
# здесь определяются константы,
# классы и функции

with open("data\\binds.pkl", 'rb') as file:
    key_mappings = pickle.load(file)

# здесь происходит инициализация,
# создание объектов
pygame.init()
pygame.font.init()
FONTS = {
    "bahnschrift": pygame.font.SysFont("bahnschrift", 20)
}
display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN, vsync=True)
clock = pygame.time.Clock()
console = Engine.Console()

in_game_input = True
draw_console = False

Map = Engine.Map("newcon3",
                 ([30, 30, 30, 30], "str", 3, 20, {"keys": ["304"]}),
                 [((100, 100, 100, 50), []), ((100, 200, 100, 50), [])],
                 [],
                 [((300, 300, 300, 300), "sand", [])],
                 [((800, 400, 500, 500), "roof.jpg", [])],
                 [((500, 500, 100, 10), "right", True, "Епта.png", "metal", [], "304")])

Map = Engine.Map.load("newcon3")

# главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            for command, key in key_mappings.items():
                if event.key == key:
                    if command == "toggle_console":
                        draw_console = not draw_console
                    elif command == "execute_command":
                        console.execute_command("map newcon3", Map)
                    elif command == "toggle_draw_rects":
                        Map.draw_rects = not Map.draw_rects
                    elif command == "interaction":
                        for obj in Map.doors:
                            x_a, y_a = Map.player.rect.center
                            x_b, y_b = obj.rect.x, obj.rect.y
                            distance = math.sqrt((x_b - x_a)**2 + (y_b - y_a)**2)
                            console.log(str(distance))
                            if distance <= 100:
                                if type(obj) == Engine.Door:
                                    obj.interact(Map.player)
                                break
                    else:
                        Map.player.move_directions[command] = True
        elif event.type == pygame.KEYUP:
            for command, key in key_mappings.items():
                if event.key == key:
                    Map.player.move_directions[command] = False
            if draw_console:
                console.event(event, Map)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for obj in Map.doors:
                    x_a, y_a = Map.player.rect.center
                    x_b, y_b = obj.rect.center
                    distance = math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
                    if distance <= 100:
                        if type(obj) == Engine.Door:
                            if obj.rect.collidepoint(event.pos[0] - Map.pos[0], event.pos[1] - Map.pos[1]):
                                obj.interact(Map.player)
                # Переместите break сюда, чтобы он выполнялся только после завершения цикла
                                break
    if in_game_input:
        Map.player.move(Map)

    Map.auto_move_map(display)
    Map.draw(display)

    if draw_console:
        console.draw(display, FONTS["bahnschrift"])

    # обновление экрана
    pygame.display.update()

    # задержка
    clock.tick(Engine.FPS)

pygame.quit()
