import numpy as np
import librosa
import pygame

def process_audio(audio_file):
    y, sr = librosa.load(audio_file, mono=True)
    normalized_signal = librosa.util.normalize(y)
    return normalized_signal, sr

def draw_waveform(screen, amplitude, WIDTH, HEIGHT, color=pygame.Color('white')):
    for i in range(len(amplitude) - 1):
        x1 = (i / len(amplitude)) * WIDTH
        x2 = ((i + 1) / len(amplitude)) * WIDTH
        y1 = HEIGHT / 2 + amplitude[i] - HEIGHT / 2
        y2 = HEIGHT / 2 + amplitude[i + 1] - HEIGHT / 2
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 1)


