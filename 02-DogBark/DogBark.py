import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    pygame.init()
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Dog Bark")

    # Prepare the image
    # Done 1: Create an image with the 2dogs.JPG image
    dog_image = pygame.image.load("2dogs.JPG")
    print("Dog image", type(dog_image))
    print("Screen", type(screen))

    # Done 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))

    # Prepare the text caption(s)
    # Done 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont("impact", 24)
    font2 = pygame.font.SysFont("phosphate", 80)
    print(pygame.font.get_fonts())
    # Done 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1 = font1.render("Two Dogs", True, (120, 0, 120))
    caption2 = font2.render("Mine!", True, (255, 255, 255))
    print("Caption", type(caption1))

    # Prepare the music
    # Done 8: Create a Sound object from the "bark.wav" file.
    dog_bark = pygame.mixer.Sound("bark.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                dog_bark.play()
            if event.type == pygame.QUIT:
                sys.exit()
            # Done 9: Play the music (bark) if there's a mouse click.

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # Done 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(dog_image, (0, 0))

        # Draw the text onto the screen
        # Done 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        screen.blit(caption1, (screen.get_width() / 2 - caption1.get_width() / 2, dog_image.get_height() + 2))

        # Done 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
        screen.blit(caption2, (screen.get_width() / 2 - caption2.get_width(), 300))

        # Update the screen
        pygame.display.update()


main()
