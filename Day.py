import pygame

class DayBlock:
    def __init__(self, date, times: list, num_days, x_pos = 15, y_pos1=100, y_pos2 = 315, color=WHITE):
        self.x_start = 15
        self.y_start = 100
        self.spacing = 20
        self.date = date
        self.times = times
        self.color = color
        self.draw()

    def draw(self):
        for day in range(self.days):
            rect = pygame.Rect(self.x_start + day*self.spacing, self.y_start, 200, 200)
            pygame.draw.rect(screen, WHITE, rect)