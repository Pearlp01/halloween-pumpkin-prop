import pygame
import random
import math

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

#Surprised expression variables
surprised = False
pupil_radius = 25          # normal size
target_pupil_radius = 25   # what it's animating toward
radius_speed = 1.5

# Angry expression variables
angry = False
top_squint = 0
target_top_squint = 0
bottom_squint = 0
target_bottom_squint = 0
squint_speed = 2

# Happy expression variables
happy =  False
happy_squint = 0
target_happy_squint = 0
squint_speed = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                surprised = not surprised
            if event.key == pygame.K_a:
                angry = not angry
                happy = False
            if event.key == pygame.K_h:
                happy = not happy
                angry = False

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

# Animate pupil size for surprised expression
    if surprised:
        target_pupil_radius = 50
    else:
        target_pupil_radius = 25

    if pupil_radius < target_pupil_radius:
        pupil_radius += radius_speed
    elif pupil_radius > target_pupil_radius:
        pupil_radius -= radius_speed

# Animate squint for angry expression
    if angry:
        target_top_squint = 40
        target_bottom_squint = 25
    else:
        target_top_squint = 0
        target_bottom_squint = 0

    if top_squint < target_top_squint:
        top_squint += squint_speed
    elif top_squint > target_top_squint:
        top_squint -= squint_speed

    if bottom_squint < target_bottom_squint:
        bottom_squint += squint_speed
    elif bottom_squint > target_bottom_squint:
        bottom_squint -= squint_speed

# Animate squint for happy expression
    if happy:
        target_happy_squint = 35
    else:
        target_happy_squint = 0

    if happy_squint < target_happy_squint:
        happy_squint += squint_speed
    elif happy_squint > target_happy_squint:
        happy_squint -= squint_speed

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
    pygame.draw.circle(screen, (0, 0, 0), (180 + pupil_x, 140 + pupil_y), pupil_radius)
    pygame.draw.circle(screen, (0, 0, 0), (380 + pupil_x, 140 + pupil_y), pupil_radius)

  # Eyelids (drawn on top, black to match background = "void" look)
    eyelid_height = int(blink_progress * 120)
    pygame.draw.rect(screen, (0, 0, 0), (120, 80, 120, eyelid_height))
    pygame.draw.rect(screen, (0, 0, 0), (320, 80, 120, eyelid_height))

# Angry squint (top and bottom close in slightly)
    pygame.draw.rect(screen, (0, 0, 0), (120, 80, 120, int(top_squint)))
    pygame.draw.rect(screen, (0, 0, 0), (320, 80, 120, int(top_squint)))
    pygame.draw.rect(screen, (0, 0, 0), (120, 200 - int(bottom_squint), 120, int(bottom_squint)))
    pygame.draw.rect(screen, (0, 0, 0), (320, 200 - int(bottom_squint), 120, int(bottom_squint)))

# Angry brows (only visible when angry)
    if angry or top_squint > 0:
        pygame.draw.line(screen, (255, 122, 26), (130, 90), (220, 105), 5)
        pygame.draw.line(screen, (255, 122, 26), (430, 90), (340, 105), 5)

# Happy Squint (bottom close in slightly)
    pygame.draw.rect(screen, (0,0,0), (120, 200 - int(happy_squint), 120, int(happy_squint)))
    pygame.draw.rect(screen, (0,0,0), (320, 200 - int(happy_squint), 120, int(happy_squint)))

#Happy brows (only visible when happy)
    if happy or happy_squint > 0:
       pygame.draw.arc(screen, (255, 122, 26), (120, 40, 120, 60), 0, math.pi, 5)
       pygame.draw.arc(screen, (255, 122, 26), (320, 40, 120, 60), 0, math.pi, 5)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()