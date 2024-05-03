import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (800x600)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color (black)
background_color = (0, 0, 0)  # RGB value for black

# Fill the screen with the background color
screen.fill(background_color)

# Load the background image (Replace 'image_directory' with the actual directory of your image)
background_image = pygame.image.load("image_directory").convert()

# Scale the background image to fit the screen resolution
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Blit (draw) the background image onto the screen surface
screen.blit(background_image, (0, 0))

# Update the display to show the background image
pygame.display.update()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.update()
