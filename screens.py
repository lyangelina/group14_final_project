import pygame
import datetime
import pygame_gui



pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
FONT_SIZE = 35



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Study Scheduler")
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, 50)

class TimeSlot:
    def __init__(self, x, y, width, height, time, duration = 60):
        self.rect = pygame.Rect(x, y, width, height)
        self.time = time
        self.duration = duration
        self.color = WHITE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 1)

        time_set = font.render(self.time.strftime("%H:%M"), True, BLACK)
        surface.blit(time_set, (self.rect.x+5, self.rect.y + 5))

class Button:
    def __init__(self, text, x_pos, y_pos, size_x, size_y, enabled, color='gray30'):
        self.rect = pygame.Rect(x_pos, y_pos, size_x, size_y)
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.enabled = enabled
        self.draw()

    def draw(self):
        text_surface = font.render(self.text, True, WHITE)
        if self.enabled:
            if self.check_click():
                pygame.draw.rect(screen, 'gray40', self.rect)
            else:
                pygame.draw.rect(screen, self.color, self.rect)
        else:
            pygame.draw.rect(screen, 'white', self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 1)
        screen.blit(text_surface, (self.x_pos + 5, self.y_pos + 12))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = self.rect
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

def draw_input_screen(exam_date, wake_time, sleep_time):

    title = title_font.render("Study Scheduler Setup", True, WHITE)
    screen.blit(title, (200, 100))

    exam_date_label = font.render("Exam Date (YYYY-MM-DD):", True, BLACK)
    screen.blit(exam_date_label, (15, 200))

    wake_time_label = font.render("Wake Up Time (HH:MM):", True, BLACK)
    screen.blit(wake_time_label, (45, 255))

    sleep_time_label = font.render("Sleep Time (HH:MM):", True, BLACK)
    screen.blit(sleep_time_label, (80, 310))

def draw_schedule_screen(time_blocks):
    screen.fill("darkslategray4")
    title = title_font.render("Your Schedule", True, WHITE)
    screen.blit(title, (290, 40))


def main():
    exam_date = ''
    wake_time = ''
    sleep_time = ''
    active_block = None
    current_screen = "input"
    time_blocks = []

    running = True
    while running:
        screen.fill('darkslategray4')

        if current_screen == "input":
            draw_input_screen(exam_date, wake_time, sleep_time)

            generate_sched_button = Button('Generate Schedule!', 275, 450, 245, 50, True, 'black')
            exam_date_input = Button(exam_date, 330, 195, 400, 40, True)
            wake_time_input = Button(wake_time, 330, 250, 400, 40, True)
            sleep_time_input = Button(sleep_time, 330, 305, 400, 40, True)

        elif current_screen == "schedule":
            draw_schedule_screen(time_blocks)

        for event in pygame.event.get():
            if current_screen == "input":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exam_date_input.rect.collidepoint(event.pos):
                        active_block = "exam"

                    elif wake_time_input.rect.collidepoint(event.pos):
                        active_block = "wake"

                    elif sleep_time_input.rect.collidepoint(event.pos):
                        active_block = "sleep"

                    else:
                        active_block =None

                    if generate_sched_button.check_click():
                        current_screen = "schedule"


                elif event.type == pygame.KEYDOWN:
                    if active_block == "exam":
                        if event.key == pygame.K_BACKSPACE:
                            exam_date = exam_date[:-1]
                        else:
                            exam_date += event.unicode

                    elif active_block == "wake":
                        if event.key == pygame.K_BACKSPACE:
                            wake_time = wake_time[:-1]
                        else:
                            wake_time += event.unicode

                    elif active_block == "sleep":
                        if event.key == pygame.K_BACKSPACE:
                            sleep_time = sleep_time[:-1]
                        else:
                            sleep_time += event.unicode

            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


        pygame.display.flip()

if __name__ == '__main__':
    main()