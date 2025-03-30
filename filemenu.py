import pygame
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename()  # Show the file open dialog
    return file_path

def draw_file_menu(screen, font):
    text = font.render("File", True, pygame.Color('white'))
    file_menu_rect = text.get_rect(topleft=(10, 10))
    screen.blit(text, file_menu_rect)
    return file_menu_rect
