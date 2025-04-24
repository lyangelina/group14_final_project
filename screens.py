import pygame
import datetime
import temp_main


pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
BLACK = (0, 0, 0)
FONT_SIZE = 35

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Study Scheduler")
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, 50)

# class TimeSlot:
#     def __init__(self, x_pos, y_pos, size_x, size_y, date, color=WHITE):
#         self.rect = pygame.Rect(x_pos, y_pos, size_x, size_y)
#         self.date = date
#         self.color = color
#         # self.draw()
#
#     def draw(self):
#         pygame.draw.rect(screen, self.color, self.rect)
#         pygame.draw.rect(screen, BLACK, self.rect, 1)
#
#         day_set = font.render(self.date, True, BLACK)
#         screen.blit(day_set, (self.rect.x+5, self.rect.y + 5))

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
#
# class DayBlocks:
#     def __init__(self, x_pos, y_pos, date_text, num_blocks):
#         self.date_text = date_text
#         self.x_pos = x_pos
#         self.y_pos = y_pos
#         self.num_blocks = num_blocks
#
#     def fill_block(self):
#         # num_blocks = list(self.num_blocks)
#         blocks_list = []
#         for block_num in range(self.num_blocks):
#             size_x = (WIDTH - 10) / self.num_blocks
#             size_y = (HEIGHT - 50) / self.num_blocks
#             blocks_list.append((block_num,pygame.Rect(self.x_pos, self.y_pos, size_x, size_y)))
#
#         for block_num, block in blocks_list:
#             pygame.draw.rect(screen, WHITE, block)



def draw_input_screen():
    title = title_font.render("Study Scheduler Setup", True, WHITE)
    screen.blit(title, (200, 100))

    exam_date_label = font.render("Exam Date (YYYY-MM-DD):", True, BLACK)
    screen.blit(exam_date_label, (15, 155))

    wake_time_label = font.render("Wake Up Time (HH:MM):", True, BLACK)
    screen.blit(wake_time_label, (45, 210))

    sleep_time_label = font.render("Sleep Time (HH:MM):", True, BLACK)
    screen.blit(sleep_time_label, (80, 265))

    busy_time_label = font.render("Busy Times (HH:MM):", True, BLACK)
    screen.blit(busy_time_label, (75, 320))

    subject_label = font.render("Subjects:", True, BLACK)
    screen.blit(subject_label, (210, 375))

def draw_schedule_screen():
    screen.fill("darkslategray4")
    title = title_font.render("Your Schedule", True, WHITE)
    screen.blit(title, (275, 40))

    # dayblocks.fill_block()

    # day_blocks = []
    # for ind_day_block, date in enumerate(range(temp_main.days)):
    #     day_blocks.append(TimeSlot(15 + ind_day_block*60 , 80, 770, 40, str(date)))
    #
    # for day in day_blocks:
    #     day.draw()



def main():
    exam_date = ''
    wake_time = ''
    sleep_time = ''
    busy_times = ''
    subjects = ''
    active_block = None
    current_screen = "input"


    running = True
    while running:
        screen.fill('darkslategray4')

        if current_screen == "input":
            draw_input_screen()
            generate_sched_button = Button('Generate Schedule!', 275, 450, 245, 50, True, 'black')
            exam_date_input = Button(exam_date, 330, 150, 400, 40, True)
            wake_time_input = Button(wake_time, 330, 205, 400, 40, True)
            sleep_time_input = Button(sleep_time, 330, 260, 400, 40, True)
            busy_time_input = Button(busy_times, 330, 315, 400, 40, True)
            subject_input = Button(subjects, 330, 370, 400, 40, True)

        elif current_screen == "schedule":
            # day_blocks = DayBlocks(20, 60, "04-23-2025", temp_main.days)
            draw_schedule_screen()


        for event in pygame.event.get():
            if current_screen == "input":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exam_date_input.rect.collidepoint(event.pos):
                        active_block = "exam"

                    elif wake_time_input.rect.collidepoint(event.pos):
                        active_block = "wake"

                    elif sleep_time_input.rect.collidepoint(event.pos):
                        active_block = "sleep"

                    elif busy_time_input.rect.collidepoint(event.pos):
                        active_block = "busy"

                    elif subject_input.rect.collidepoint(event.pos):
                        active_block = "subject"

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

                    elif active_block == "busy":
                        if event.key == pygame.K_BACKSPACE:
                            busy_times= busy_times[:-1]
                        else:
                            busy_times += event.unicode

                    elif active_block == "subject":
                        if event.key == pygame.K_BACKSPACE:
                            subjects = subjects[:-1]
                        else:
                            subjects += event.unicode

            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


        pygame.display.flip()

if __name__ == '__main__':
    main()