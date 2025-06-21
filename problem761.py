# https://projecteuler.net/problem=761
import time

import numpy as np
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display surface
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Animate Circle")

# is point c left of line a->b
def is_left(a, b, c):
  return (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0]) > 0

# distance between two polar coordinates (swimmer to poolside)
def distance(r1, angle1, r2, angle2):
    return math.sqrt(r1*r1 + r2*r2 - 2*r1*r2*math.cos(angle1-angle2))

# distance between two angles over the circle (runner to swimmer)
def arc_length(r, angle1, angle2):
    # https://stackoverflow.com/questions/61479191/convert-any-angle-to-the-interval-pi-pi
    angle = math.remainder(angle2 - angle1, 2*math.pi)
    return abs(angle * r)



# Main game loop
def main():
    running = True
    clock = pygame.time.Clock()

    # Initial position and velocity for the green circle
    green_circle_radius = 10
    swimmer_x = 0
    swimmer_y = 0
    swimmer_velocity_x = -1
    swimmer_velocity_y = 0
    pool_radius = 100
    runner_angle = 0
    runner_velocity = 5.05 # 4.05 max
    runner_direction = 1

    runner_x = pool_radius
    runner_y = 0

    update = False

    counter = 0

    while running:
        counter += 1
        if counter == 1:
            update = True
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white color
        screen.fill(WHITE)

        # Draw pool
        pygame.draw.circle(screen, BLACK, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), pool_radius, 2)

        if update:
            # Update runner
            d_angle = runner_velocity / pool_radius * runner_direction

            # TODO: bereken + en -, en kies degene die de afstand kleiner maakt
            runner_angle += d_angle

            runner_x = pool_radius * math.cos(runner_angle)
            runner_y = pool_radius * math.sin(runner_angle)


            # Update swimmer

            # other side of red TODO: fix for circle origin
            # dx = (WINDOW_WIDTH // 2 - c_dx) - green_circle_x
            # dy = (WINDOW_HEIGHT // 2 - c_dy) - green_circle_y
            # norm_xy = math.sqrt(dx * dx + dy * dy)
            # swimmer_velocity_x = dx / norm_xy
            # swimmer_velocity_y = dy / norm_xy



            swimmer_r = math.sqrt((swimmer_x) ** 2 + (swimmer_y) ** 2)
            swimmer_angle = math.atan2(swimmer_y, swimmer_x)

            angles = []
            STEPS = 10000
            for p in range(STEPS):
                theta = (p / STEPS) * math.tau

                d_swim = distance(swimmer_r, swimmer_angle, pool_radius, theta)

                d_run = arc_length(pool_radius, runner_angle, theta)

                angles.append((d_run / d_swim, theta))

            score, best_pool_angle = max(angles)
            # print(angles)
            # print(best_pool_angle)



            # swim away (calculate vector from runner to swimmer and normalize to speed 1)
            # dx = swimmer_x - runner_x
            # dy = swimmer_y - runner_y

            # swim to optimum runner/swimmer ratio
            tx = pool_radius * math.cos(best_pool_angle)
            ty = pool_radius * math.sin(best_pool_angle)
            dx = tx - swimmer_x
            dy = ty - swimmer_y
            norm_xy = math.sqrt(dx*dx + dy*dy)
            swimmer_velocity_x = dx / norm_xy
            swimmer_velocity_y = dy / norm_xy
            swimmer_x += swimmer_velocity_x
            swimmer_y += swimmer_velocity_y


            # stop if swimmer reached circle
            if swimmer_r >= pool_radius:
                update = False

        # draw runner and swimmer
        pygame.draw.circle(screen, RED, (WINDOW_WIDTH // 2 + int(runner_x), WINDOW_HEIGHT // 2 + int(runner_y)), 10)
        pygame.draw.circle(screen, GREEN, (WINDOW_WIDTH // 2 + int(swimmer_x), WINDOW_HEIGHT // 2 + int(swimmer_y)), green_circle_radius)

        # calculate shortest side around the pool to swimmer
        if is_left((0, 0), (runner_x, runner_y),
                   (swimmer_x, swimmer_y)):
            runner_direction = 1
        else:
            runner_direction = -1

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
