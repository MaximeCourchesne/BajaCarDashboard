import pygame
from dashboard.Utils import load_settings

class FuelBar:
    def __init__(self, window, position=(50, 300), width=200, height=30, full_color=(0, 255, 0), empty_color=(255, 0, 0), border_color=[0, 0, 0], border_width=3):
        self.window = window
        self.position = position
        self.width = width
        self.height = height
        self.full_color = full_color
        self.empty_color = empty_color
        self.border_color = border_color
        self.border_width = border_width
        settings = load_settings("config/settings.json")
        self.fuel_level = settings["fuel_bar"]["initial_level"]



    def update_fuel_level(self, level):
        self.fuel_level = max(0.0, min(level, 1.0))

    def draw_gradient(self):
        x, y = self.position
        for i in range(self.width):

            t = i / self.width
            color = (
                int(self.empty_color[0] + (self.full_color[0] - self.empty_color[0]) * t),
                int(self.empty_color[1] + (self.full_color[1] - self.empty_color[1]) * t),
                int(self.empty_color[2] + (self.full_color[2] - self.empty_color[2]) * t),
            )
            
            if i < int(self.width * self.fuel_level):
                pygame.draw.line(self.window, color, (x + i, y), (x + i, y + self.height))

    def display(self):
        self.draw_gradient()
        pygame.draw.rect(self.window, self.border_color, (*self.position, self.width, self.height), self.border_width)

