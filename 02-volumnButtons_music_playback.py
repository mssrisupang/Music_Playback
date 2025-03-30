import pygame
import sys

# Initialize PyGame and the mixer
pygame.init()
pygame.mixer.init()

# Load  music file
audio_file = 'StarWars60.wav'
pygame.mixer.music.load(audio_file)


# Set up the display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

# Button dimensions
button_width, button_height = 100, 50

# initial volume
current_volume = pygame.mixer.music.get_volume()  # Initial volume

# Play button
play_button = pygame.Rect(WIDTH // 4 - button_width // 2, HEIGHT // 2 - button_height // 2, button_width, button_height)

# Pause button
pause_button = pygame.Rect(2 * WIDTH // 4 - button_width // 2, HEIGHT // 2 - button_height // 2, button_width, button_height)

# Stop button
stop_button = pygame.Rect(3 * WIDTH // 4 - button_width // 2, HEIGHT // 2 - button_height // 2, button_width, button_height)

# Volume button dimensions and positions
volume_up_button = pygame.Rect(WIDTH // 6 - button_width // 2, HEIGHT - 75, button_width, button_height)
volume_down_button = pygame.Rect(5 * WIDTH // 6 - button_width // 2, HEIGHT - 75, button_width, button_height)


def draw_buttons():
    # Draw the play button
    pygame.draw.rect(screen, GREEN, play_button)
    play_text = font.render('Play', True, WHITE)
    screen.blit(play_text, (play_button.x + 20, play_button.y + 10))
    
    # Draw the pause button
    pygame.draw.rect(screen, BLUE, pause_button)
    pause_text = font.render('Pause', True, WHITE)
    screen.blit(pause_text, (pause_button.x + 10, pause_button.y + 10))

    # Draw the stop button
    pygame.draw.rect(screen, RED, stop_button)
    stop_text = font.render('Stop', True, WHITE)
    screen.blit(stop_text, (stop_button.x + 10, stop_button.y + 10))

    # Draw the volume up button
    pygame.draw.rect(screen, GREEN, volume_up_button)
    volume_up_text = font.render('+', True, WHITE)
    screen.blit(volume_up_text, (volume_up_button.x + 40, volume_up_button.y + 10))
    
    # Draw the volume down button
    pygame.draw.rect(screen, RED, volume_down_button)
    volume_down_text = font.render('-', True, WHITE)
    screen.blit(volume_down_text, (volume_down_button.x + 40, volume_down_button.y + 10))

# Main game loop
running = True
Status  = True
font = pygame.font.Font(None, 36)
while running:
    current_volume = pygame.mixer.music.get_volume()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                pygame.mixer.music.play()  
            elif pause_button.collidepoint(event.pos):
                if Status == True:
                    pygame.mixer.music.pause()
                    Status = False
                else:
                    if Status==False:
                        pygame.mixer.music.unpause()
                        Status=True
            elif stop_button.collidepoint(event.pos):
                pygame.mixer.music.stop()

            elif volume_up_button.collidepoint(event.pos):
                current_volume = min(1.0, current_volume + 0.1)  # Increase volume, max out at 1.0
                print(current_volume)
                pygame.mixer.music.set_volume(current_volume)
            elif volume_down_button.collidepoint(event.pos):
                current_volume = max(0.0, current_volume - 0.1)  # Decrease volume, min out at 0.0
                pygame.mixer.music.set_volume(current_volume)
                print(current_volume)

    screen.fill((0, 0, 0))  # Fill the screen with black
    draw_buttons()
    pygame.display.update()

pygame.quit()
sys.exit()
