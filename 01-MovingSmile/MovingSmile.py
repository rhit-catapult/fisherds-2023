import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))

    is_nose_drawn = False
    is_mouth_drawn = True
    eye_delta_x = 0
    eye_delta_y = 0

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                is_nose_drawn = True
            if event.type == pygame.MOUSEBUTTONUP:
                is_nose_drawn = False
            if event.type == pygame.KEYDOWN:
                is_mouth_drawn = False
                if event.scancode == 79:
                    eye_delta_x += 1
                if event.scancode == 80:
                    eye_delta_x -= 1
                if event.scancode == 81:
                    eye_delta_y += 1
                if event.scancode == 82:
                    eye_delta_y -= 1

            if event.type == pygame.KEYUP:
                is_mouth_drawn = True
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))  # white

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            eye_delta_y -= 1
        if keys_pressed[pygame.K_a]:
            eye_delta_x -= 1
        if keys_pressed[pygame.K_s]:
            eye_delta_y += 1
        if keys_pressed[pygame.K_d]:
            eye_delta_x += 1

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + eye_delta_x, 162 + eye_delta_y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + eye_delta_x, 162 + eye_delta_y), 7)  # black pupil

        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
        if is_nose_drawn:
            pygame.draw.circle(screen, (80, 0, 0), (320, 245), 10)

        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        if is_mouth_drawn:
            pygame.draw.rect(screen, (0, 0, 0), (230, 320, 180, 30))

        pygame.display.update()


main()
