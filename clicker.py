import pygame
import time


class Parameter:
    value = 0
    key_ = pygame.K_SPACE
    place_ = 0
    text_ = ""
    last_time = 0


pygame.init()

sc = pygame.display.set_mode((800, 600))
sc.fill((200, 255, 200))

font = pygame.font.Font(None, 72)
font1 = pygame.font.Font(None, 36)

p1 = Parameter()
p2 = Parameter()
p3 = Parameter()
p4 = Parameter()
p5 = Parameter()
p6 = Parameter()
p3.value = 1

clicks = 0

latest = time.time()
text = font.render("0", 1, (0, 100, 0))
place = text.get_rect(center=(400, 300))
p1.place_ = text.get_rect(center=(50, 50))
p2.place_ = text.get_rect(center=(50, 350))
p3.place_ = text.get_rect(center=(50, 150))
p4.place_ = text.get_rect(center=(50, 450))
p5.place_ = text.get_rect(center=(50, 250))
p6.place_ = text.get_rect(center=(50, 550))

p1.key_ = pygame.K_a
p2.key_ = pygame.K_b
p3.key_ = pygame.K_c
p4.key_ = pygame.K_d
p5.key_ = pygame.K_e
p6.key_ = pygame.K_f

p1.text_ = "Hand clicks: "
p2.text_ = "Auto clicks: "
p3.text_ = "Hand coefficient: "
p4.text_ = "Auto coefficient: "
p5.text_ = "Real number of clicks: "
p6.text_ = "Time: "

ps = [p1, p2, p3, p4, p5, p6]

sc.blit(text, place)

pygame.display.update()
start = time.time()

while 1:
    ps[5].value = int(time.time() - start)
    sc.fill((200, 255, 200))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:

            if i.key == pygame.K_SPACE:
                clicks += ps[2].value
                ps[0].value += ps[2].value
                ps[4].value += 1

            elif i.key == pygame.K_UP and clicks >= 10:
                clicks -= 10
                ps[2].value += 1
                ps[4].value += 1
            elif i.key == pygame.K_RIGHT and clicks >= 100:
                clicks -= 100
                ps[3].value += 1
                ps[4].value += 1
            elif i.key == pygame.K_LSHIFT:
                for j in ps:
                    j.last_time = time.time()
            else:
                for j in ps:
                    if i.key == j.key_:
                        j.last_time = time.time()

    if time.time() - latest >= 1:
        clicks += ps[3].value
        ps[1].value += ps[3].value
        latest = time.time()

    for j in ps:
        if time.time() - j.last_time <= 5:
            local_text = font1.render(j.text_ + str(j.value), 1, (0, 100, 0))
            sc.blit(local_text, j.place_)

    text = font.render(str(clicks), 1, (0, 100, 0))

    sc.blit(text, place)

    pygame.display.update()
