#4286.5
import pygame
import sys
import random
import time

def main():
    pygame.init()
    screen_size = 900
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Drawing!")

    num = 0
    clock = pygame.time.Clock()
    big_text = ''
    font = pygame.font.Font(None, 170)
    background = pygame.image.load('drawing.jpeg')
    background = pygame.transform.scale(background, (screen_size, screen_size))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_SPACE]:
                    num = random.randint(1, 8573)
                    # print(num)
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (254, 230, 70), (50, 300, 400, 100))
        num_str = str(num).zfill(5)
        big_text = num_str
        caption = font.render(big_text, True, (0, 0, 0))
        screen.blit(caption, (65, 290))





        pygame.display.update()


main()
