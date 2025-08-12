import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gyors Gamer kör")

clock = pygame.time.Clock()
running = True
t = 0

# Kör paraméterek
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_vx, ball_vy = 15, 12  # nagyon gyors mozgás
ball_radius = 30
ball_border_color = (0, 255, 0)  # neon zöld
ball_fill_color = (0, 0, 0)      # fekete

def smooth_color(x, y, t):
    r = int((math.sin(x/50 + t) + 1) * 127.5)
    g = int((math.sin(y/50 + t + 2) + 1) * 127.5)
    b = int((math.sin((x + y)/70 + t + 4) + 1) * 127.5)
    return (r, g, b)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Háttér
    for y in range(HEIGHT):
        for x in range(WIDTH):
            screen.set_at((x, y), smooth_color(x, y, t))

    # Labda mozgás
    ball_x += ball_vx
    ball_y += ball_vy

    # Pattogás
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_vx *= -1
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_vy *= -1

    # Labda kirajzolása
    pygame.draw.circle(screen, ball_fill_color, (int(ball_x), int(ball_y)), ball_radius)
    pygame.draw.circle(screen, ball_border_color, (int(ball_x), int(ball_y)), ball_radius, 3)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS
    t += 0.05

pygame.quit()