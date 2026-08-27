import pygame

pygame.init()

screen = pygame.display.set_mode((560, 280))
pygame.display.set_caption("Eye Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 122, 26), (180, 140), 60)
    pygame.draw.circle(screen, (255, 122, 26), (380, 140), 60)
    pygame.draw.circle(screen, (0, 0,0), (180, 140), 25)
    pygame.draw.circle(screen, (0, 0, 0), (380, 140), 25)
    pygame.display.flip()

pygame.quit()