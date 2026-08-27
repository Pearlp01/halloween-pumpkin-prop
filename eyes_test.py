import pygame

pygame.init()

screen = pygame.display.set_mode((560, 280))
pygame.display.set_caption("Eye Test")
clock = pygame.time.Clock()

# Pupil position (starts centered)
pupil_x = 0
pupil_y = 0
move_speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Check which keys are currently held down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pupil_x -= move_speed
    if keys[pygame.K_RIGHT]:
        pupil_x += move_speed
    if keys[pygame.K_UP]:
        pupil_y -= move_speed
    if keys[pygame.K_DOWN]:
        pupil_y += move_speed

    screen.fill((0, 0, 0))

# Eyes (fixed position)
    pygame.draw.circle(screen, (255, 122, 26), (180, 140), 60)
    pygame.draw.circle(screen, (255, 122, 26), (380, 140), 60)

 # Pupils (position = base position + offset)
    pygame.draw.circle(screen, (0, 0, 0), (180 + pupil_x, 140 + pupil_y), 25)
    pygame.draw.circle(screen, (0, 0, 0), (380 + pupil_x, 140 + pupil_y), 25)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()