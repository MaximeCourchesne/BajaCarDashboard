import pygame
import math

class RPMBar:
    def __init__(self, window, position=(200, 200), radius=100, width=9, color=(255, 0, 0)):
        self.window = window
        self.position = position
        self.radius = radius
        self.width = width
        self.color = color
        self.rpm_value = 0.8*0.7

    def update_rpm(self, rpm):
        self.rpm_value = max(0.0, min(rpm, 1.0))
        
    def display(self):
        start_angle = math.radians(180 - 180 * self.rpm_value)
        end_angle = start_angle + math.radians(180 * self.rpm_value)

        # drawing contour
        pygame.draw.arc(
            self.window,
            (0, 0, 0),
            (self.position[0] - self.radius - 1, self.position[1] - self.radius - 1, 
            2 * (self.radius + 1), 2 * (self.radius + 1)),
            start_angle,
            end_angle,
            self.width + 2
        )

        # drawing main arc
        pygame.draw.arc(
            self.window,
            self.color,
            (self.position[0] - self.radius, self.position[1] - self.radius, 2 * self.radius, 2 * self.radius),
            start_angle,
            end_angle,
            self.width
        )
        

