import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
FONT_SIZE = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Study Scheduler")
font = pygame.font.Font(None, FONT_SIZE)

class TimeSlot:
    def __init__(self, x, y, width, height, time, duration = 60):
        self.rect = pygame.Rect(x, y, width, height)
        self.time = time
        self.duration = duration
        self.color = WHITE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 1)


def main():
    user_input = ''
    user_input_active = False
    active_block = None

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        screen.fill('BLUE')
        pygame.display.flip()

if __name__ == '__main__':
    main()