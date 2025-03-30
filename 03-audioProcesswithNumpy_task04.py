import numpy as np
import librosa
import pygame
import sys

# Initialize PyGame
pygame.init()
pygame.mixer.init()

# Set up the display
WIDTH, HEIGHT = 800, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Audio Signal Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def process_audio(audio_file):
    # Load audio file with librosa; y is the audio signal, sr is the sample rate
    y, sr = librosa.load(audio_file, mono=True)
    # Example processing: Simple normalization (not necessary for visualization)
    normalized_signal = librosa.util.normalize(y)
    return normalized_signal, sr


# Process Audio
audio_file = 'gettysburg10.wav'
signal, sr = process_audio(audio_file)
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(-1)  # The -1 argument makes the music loop indefinitely
#print(signal[:10], sr)

# Normalize the signal's amplitude to the height of the window
amplitude = np.interp(signal, (signal.min(), signal.max()), (0, HEIGHT))


def draw_waveform(screen, amplitude):
    for i in range(len(amplitude) - 1):
        # Scale x positions to fit the screen
        x1 = (i / len(amplitude)) * WIDTH
        x2 = ((i + 1) / len(amplitude)) * WIDTH
        y1 = HEIGHT / 2 + amplitude[i] - HEIGHT / 2
        y2 = HEIGHT / 2 + amplitude[i + 1] - HEIGHT / 2
        pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
        elif event.type == pygame.KEYDOWN:
              # Stop music if the 's' key is pressed
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
             # Play music if the 'p' key is pressed
            if event.key == pygame.K_p:
                pygame.mixer.music.play()

    screen.fill(BLACK)  # Fill the screen with black
    draw_waveform(screen, amplitude)
    pygame.display.update()

pygame.quit()
sys.exit()
