import numpy as np
import librosa
import pygame
import sys
import tkinter as tk
from tkinter import filedialog   

# Initialize PyGame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Audio Signal Visualization")
font = pygame.font.Font(None, 36)  
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

def open_file_dialog():
    root = tk.Tk()   # initial
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename()  # Show the file open dialog
    return file_path


def draw_file_menu(screen, font):
    global file_menu_rect  # Global, so it's accessible outside this function for click detection
    text = font.render("File", True, WHITE)
    file_menu_rect = text.get_rect(topleft=(10, 10))
    screen.blit(text, file_menu_rect)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if  file_menu_rect.collidepoint(event.pos):
                audio_file = open_file_dialog()
                if audio_file:  # Make sure a file was selected
                    signal, sr = process_audio(audio_file)
                    amplitude = np.interp(signal, (signal.min(), signal.max()), (0, HEIGHT))
                    pygame.mixer.music.load(audio_file)
                    pygame.mixer.music.play(-1)

    screen.fill(BLACK)  # Fill the screen with black
    draw_file_menu(screen, font)
    draw_waveform(screen, amplitude)
    pygame.display.update()

pygame.quit()
sys.exit()
