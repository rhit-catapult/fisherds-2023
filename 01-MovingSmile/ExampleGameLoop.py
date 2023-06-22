import pygame
import sys


pygame.init()
pygame.display.set_caption("Dave Fisher")
screen = pygame.display.set_mode((640, 480))

# TODO 05: Change the window size, make sure your circle code still works.

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            print("Goodbye!!!!")
            sys.exit()

        # Additional interactions with events

    screen.fill(pygame.Color("darkgreen"))
    screen.fill((128, 0, 0))

    # Draw things on the screen

    # TODO 02: Try to draw a circle (any size, any color, anywhere)
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("yellow"), (50, 300), 10)

    # TODO 03: Try to draw a red circle in the middle of the screen with a radius 100
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("red"), (screen.get_width() / 2, screen.get_height() / 2), 100)

    # TODO 04: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )

    # This will make sure that things appear on our screen, without this
    # update, everything we do will not be visible!
    # notice how this statement is still inside of the first while loop, but
    # outside of the for loop (why? because it is at the same level of
    # indentation as the for loop statement).
    pygame.display.update()
