import pygame
import time

pygame.init()

sc = pygame.display.set_mode((400, 300))
sc.fill((200, 255, 200))

font = pygame.font.Font(None, 72)
clicks = 0
coefficient = 1
auto = 0
latest = time.time()
text = font.render("0", 1, (0, 100, 0))
place = text.get_rect(center=(200, 150))
sc.blit(text, place)

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:

            if i.key == pygame.K_SPACE:
                clicks += coefficient
                text = font.render(str(clicks), 1, (0, 100, 0))
            elif i.key == pygame.K_UP and clicks >= 10:
                clicks -= 10
                coefficient += 1
                text = font.render(str(clicks), 1, (0, 100, 0))
            elif i.key == pygame.K_RIGHT and clicks >= 100:
                clicks -= 100
                auto += 1
                text = font.render(str(clicks), 1, (0, 100, 0))
    if time.time() - latest >= 1:
        clicks += auto
        latest = time.time()
    text = font.render(str(clicks), 1, (0, 100, 0))
    sc.fill((200, 255, 200))
    sc.blit(text, place)

    pygame.display.update()
