import pygame
import random

pygame.init()

screen = pygame.display.set_mode((560, 280))
pygame.display.set_caption("Eye Test")
clock = pygame.time.Clock()
max_offset = 35

# Pupil position (starts centered)
pupil_x = 0
pupil_y = 0
move_speed = 3

# Blink variables
blink_timer = 0
next_blink = random.randint(120, 300)
blinking = False
blink_closing = True
blink_progress = 0  # 0 = fully open, 1 = fully closed
blink_speed = 0.05

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

# Keep pupil within the eye
    distance = (pupil_x**2 + pupil_y**2) ** 0.5
    if distance > max_offset:
        scale = max_offset / distance
        pupil_x *= scale
        pupil_y *= scale

# Decide when to start a blink
    blink_timer += 1
    if not blinking and blink_timer >= next_blink:
        blinking = True
        blink_closing = True

 # Animate the blink itself
    if blinking:
        if blink_closing:
            blink_progress += blink_speed
            if blink_progress >= 1:
                blink_progress = 1
                blink_closing = False
        else:
            blink_progress -= blink_speed
            if blink_progress <= 0:
                blink_progress = 0
                blinking = False
                blink_timer = 0
                next_blink = random.randint(120, 300)


    screen.fill((0, 0, 0))

# Eyes (fixed position)
    pygame.draw.circle(screen, (255, 122, 26), (180, 140), 60)
    pygame.draw.circle(screen, (255, 122, 26), (380, 140), 60)

 # Pupils (position = base position + offset)
    pygame.draw.circle(screen, (0, 0, 0), (180 + pupil_x, 140 + pupil_y), 25)
    pygame.draw.circle(screen, (0, 0, 0), (380 + pupil_x, 140 + pupil_y), 25)

  # Eyelids (drawn on top, black to match background = "void" look)
    eyelid_height = int(blink_progress * 120)
    pygame.draw.rect(screen, (0, 0, 0), (120, 80, 120, eyelid_height))
    pygame.draw.rect(screen, (0, 0, 0), (320, 80, 120, eyelid_height))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()