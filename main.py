import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
BACKGROUND_COLOR = (255, 255, 255)
POINT_COLOR = (0, 0, 0)
LINE_COLOR = (255, 0, 0)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 24

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Distance Calculator")

# Fonts
font = pygame.font.Font(None, FONT_SIZE)

# Points
point1 = None
point2 = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if point1 is None:
                point1 = event.pos
            else:
                point2 = event.pos

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw points
    if point1:
        pygame.draw.circle(screen, POINT_COLOR, point1, 5)
    if point2:
        pygame.draw.circle(screen, POINT_COLOR, point2, 5)

    # Draw line and calculate distance if both points are selected
    if point1 and point2:
        pygame.draw.line(screen, LINE_COLOR, point1, point2)
        distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
        text = font.render(f"Distance: {distance:.2f} miles", True, FONT_COLOR)
        screen.blit(text, (10, 10))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
