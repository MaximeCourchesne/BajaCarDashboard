import pygame
from dashboard.Utils import load_settings

class Digit:
    def __init__(self, window, position=(50, 50), segment_length=100, segment_width=15):
        self.window = window
        self.position = position
        self.segment_length = segment_length
        self.segment_width = segment_width
        settings = load_settings("config/settings.json")
        self.segment_off_color = settings["digit"]["off_color"]
        self.segment_on_color = settings["digit"]["on_color"]
        
        # Define positions the segments positions
        x, y = position
        self.segments = {
            'A': [(x, y - segment_width), (segment_length, segment_width)],
            'B': [(x + segment_length, y), (segment_width, segment_length)],
            'C': [(x + segment_length, y + segment_length + segment_width), (segment_width, segment_length)],
            'D': [(x, y + 2 * segment_length + segment_width), (segment_length, segment_width)],
            'E': [(x - segment_width, y + segment_length + segment_width), (segment_width, segment_length)],
            'F': [(x - segment_width, y), (segment_width, segment_length)],
            'G': [(x, y + segment_length), (segment_length, segment_width)],
        }
        
        self.segment_map = {
            0: ['A', 'B', 'C', 'D', 'E', 'F'],
            1: ['B', 'C'],
            2: ['A', 'B', 'G', 'E', 'D'],
            3: ['A', 'B', 'G', 'C', 'D'],
            4: ['F', 'G', 'B', 'C'],
            5: ['A', 'F', 'G', 'C', 'D'],
            6: ['A', 'F', 'G', 'C', 'D', 'E'],
            7: ['A', 'B', 'C'],
            8: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            9: ['A', 'B', 'C', 'D', 'F', 'G'],
        }

        # Current digit to display
        self.current_digit = 0

    def set_digit(self, digit):
        if digit in self.segment_map:
            self.current_digit = digit
        else:
            raise ValueError(f"Invalid digit {digit}. Must be between 0 and 9.")

    def draw_segment(self, pos, size, color):
        """Draw a single segment on the display."""
        pygame.draw.rect(self.window, color, (*pos, *size), border_radius=5)

    def display(self):
        # Turn off all segments
        for pos, size in self.segments.values():
            self.draw_segment(pos, size, self.segment_off_color)
        
        # Turn on segments for the current digit
        for segment in self.segment_map.get(self.current_digit, []):
            pos, size = self.segments[segment]
            self.draw_segment(pos, size, self.segment_on_color)
