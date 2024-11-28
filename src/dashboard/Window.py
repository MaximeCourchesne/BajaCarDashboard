import pygame
from dashboard.Utils import load_settings, load_image
from dashboard.Digit import Digit
from dashboard.FuelBar import FuelBar
from dashboard.RPMBar import RPMBar
from dashboard.SpeedDigits import SpeedDigits


class Window:
    def __init__(self, settings_path="config/settings.json"):
        # Load settings from config/settings.json
        self.settings = load_settings(settings_path)
        self.width = self.settings["window"]["width"]
        self.height = self.settings["window"]["height"]
        self.background_color = tuple(self.settings["window"]["background_color"])

        # Initialize pygame window
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Baja Dashboard")
        self.running = True

        self.speed_digits = SpeedDigits(self.window, position0=(50, 50), position1=(210, 50), segment_length=100, segment_width=15)

        self.current_digit = 0
        self.fuel_bar = FuelBar(
            self.window,
            position=(50, 300),
            width=500,
            height=30,
            full_color=tuple(self.settings["fuel_bar"]["full_color"]),
            empty_color=tuple(self.settings["fuel_bar"]["empty_color"]),
            border_color=self.settings["fuel_bar"]["border_color"],
            border_width=self.settings["fuel_bar"]["border_width"],
        )
        self.rpm_bar = RPMBar(self.window, position=(200, 200))

        self.logo = load_image("assets/images/mcgill_logo.png", (1200/6, 1523/6))




    # testing functions for displaying fuel and speed
    def keyboard_events_for_testing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_digit = (self.current_digit + 1) % 100
                elif event.key == pygame.K_DOWN:
                    self.current_digit = (self.current_digit - 1) % 100
                elif event.key == pygame.K_RIGHT:
                    self.fuel_bar.update_fuel_level(self.fuel_bar.fuel_level + 0.1)
                elif event.key == pygame.K_LEFT:
                    self.fuel_bar.update_fuel_level(self.fuel_bar.fuel_level - 0.1)


    def clear_screen(self):
        self.window.fill(self.background_color)

    def update_display(self):
        pygame.display.flip()

    def display_image(self, image, position):
        if image:
            self.window.blit(image, position)


    def run(self):
        while self.running:
            self.keyboard_events_for_testing()
            self.clear_screen()
            
            self.speed_digits.set_speed(self.current_digit)
            self.speed_digits.display()

            self.display_image(self.logo, (self.width - 210, self.height - 290))  # Position near the top right
            self.fuel_bar.display()
            # RPM bar not fully working yet
            # self.rpm_bar.display()

            self.update_display()

        pygame.quit()
