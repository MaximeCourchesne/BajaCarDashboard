import json
import pygame
# helper functions

def load_settings(file_path="config/settings.json"):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_image(image_path, size=None):
    try:
        image = pygame.image.load(image_path)
        if size:
            image = pygame.transform.scale(image, size)
        return image
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return None