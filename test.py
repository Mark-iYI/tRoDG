import pygame
import sys

# Инициализация Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Инициализация шрифтов
pygame.font.init()
font = pygame.font.Font(None, 24)

# Переменные для ввода текста
input_active = False
input_text = ''
input_rect = pygame.Rect(10, height - 40, 140, 30)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

# Функция для отображения текста
def draw_text(surface, text, font, color, rect, text_input):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (rect.x + 5, rect.y + 5))
    pygame.draw.rect(surface, color, rect, 2)
    if text_input:
        pygame.draw.rect(surface, color, rect, 2)

# Главный цикл игры
running = True
while running:
    screen.fill((30, 30, 30))  # Задаем фон

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False
            color = color_active if input_active else color_inactive
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    print(input_text)  # Вывод введенного текста в консоль (вы можете изменить на вашу логику обработки введенного текста)
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    draw_text(screen, '>>> ' + input_text, font, color, input_rect, input_active)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
