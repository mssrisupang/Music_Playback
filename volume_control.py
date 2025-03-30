# volume_control.py

import pygame

def increase_volume(current_volume, increment=0.1):
    new_volume = min(1.0, current_volume + increment)
    pygame.mixer.music.set_volume(new_volume)
    return new_volume

def decrease_volume(current_volume, decrement=0.1):
    new_volume = max(0.0, current_volume - decrement)
    pygame.mixer.music.set_volume(new_volume)
    return new_volume
