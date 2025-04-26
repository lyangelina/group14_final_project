import pygame
import datetime
import temp_main


pygame.init()
pygame.key.set_repeat(300, 200)

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
BLACK = (0, 0, 0)
FONT_SIZE = 35

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Study Scheduler")
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, 50)
pop_up_font = pygame.font.Font(None, 25)
blocks_info_font = pygame.font.Font(None, 22)


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


class DayBlock:
    """
    def __init__(self, date_str, times: [], x_start =15, y_start = 80):
        self.x_start = x_start
        self.y_start = y_start
        self.color = WHITE

    def shift_box_x(self):
        self.x_start += 215
    """
    def __init__(self, date_str, x_start = 15, y_start = 80):
        self.x_start = x_start
        self.y_start = y_start
        self.date_str = date_str
        # self.times = times
        self.color = WHITE


    def draw(self):
        rect = pygame.Rect(self.x_start, self.y_start, 250, 250)
        pygame.draw.rect(screen, WHITE, rect)

        date_font = blocks_info_font.render(self.date_str, True, BLACK)
        screen.blit(date_font, (self.x_start + 10, self.y_start + 10))


def draw_input_screen():
    def draw_input_screen():
    """
    Draws initial input screen for study schedule 
    Function renders and displays the title and input labels on the screen:
        - Exam date
        - Wake up time
        - Sleep time
        - Study times
        - Subjects
    
    """
    title = title_font.render("Study Scheduler Setup", True, WHITE)
    screen.blit(title, (200, 100))

    exam_date_label = font.render("Exam Date (YYYY-MM-DD):", True, BLACK)
    screen.blit(exam_date_label, (15, 155))

    wake_time_label = font.render("Wake Up Time (HH:MM):", True, BLACK)
    screen.blit(wake_time_label, (45, 210))

    sleep_time_label = font.render("Sleep Time (HH:MM):", True, BLACK)
    screen.blit(sleep_time_label, (80, 265))

    study_time_label = font.render("Study Times (HH:MM):", True, BLACK)
    screen.blit(study_time_label, (62, 320))

    subject_label = font.render("Subjects:", True, BLACK)
    screen.blit(subject_label, (210, 375))

def draw_schedule_screen(exam_date):
    screen.fill("darkslategray4")
    title = title_font.render("Your Schedule", True, WHITE)
    screen.blit(title, (275, 40))

    curr_date = datetime.date.today()
    exam_date_obj = datetime.date(int(exam_date[0:4]), int(exam_date[5:7]), int(exam_date[8:]))
    days_till = (exam_date_obj - curr_date).days
    # temp_main.days = days_till
    dates = []
    for days_past in range(days_till+1):
        date_obj = curr_date + datetime.timedelta(days=days_past)
        date_str = date_obj.strftime('%Y-%m-%d')
        dates.append(date_str)

    x_pos = 10
    for day,date in enumerate(dates):
        if day < 3:
            box = DayBlock(date, x_pos)
            box.draw()
            x_pos += 265

        if 3 <= day <= 5:
            if day == 3:
                x_pos = 10
                y_pos = 340
            box = DayBlock(date, x_pos, y_pos)
            box.draw()
            x_pos += 265


def pop_up_window():
    screen.fill("darkslategray4")


    message = pop_up_font.render("You have plenty of time! Choose a date within 6 days!", True, BLACK)
    pop_up = pygame.Rect(180, 250, 450, 60)
    pygame.draw.rect(screen, WHITE, pop_up)
    screen.blit(message, (185, 270))



def check_date(exam_date, curr_date=None):
    curr_date = datetime.date.today()
    exam_date_obj = datetime.date(int(exam_date[0:4]), int(exam_date[5:7]), int(exam_date[8:]))
    days_till = (exam_date_obj - curr_date).days
    if days_till < 0 or days_till > 6:
        return True
    else:
        return


def main():
    exam_date = ''
    wake_time = ''
    sleep_time = ''
    study_times = ''
    subjects = ''
    active_block = None
    current_screen = "input"


    running = True
    exam_date_str =""
    while running:
        screen.fill('darkslategray4')

        if current_screen == "input":
            draw_input_screen()
            generate_sched_button = Button('Generate Schedule!', 275, 450, 245, 50, True, 'black')
            exam_date_input = Button(exam_date, 330, 150, 400, 40, True)
            wake_time_input = Button(wake_time, 330, 205, 400, 40, True)
            sleep_time_input = Button(sleep_time, 330, 260, 400, 40, True)
            study_time_input = Button(study_times, 330, 315, 400, 40, True)
            subject_input = Button(subjects, 330, 370, 400, 40, True)

        elif current_screen == "schedule":
            draw_schedule_screen(exam_date)

        elif current_screen == "pop up":
            pop_up_window_button = Button("You have plenty of time! Enter a date within 6 days.", 180, 250, 450, 60, True, 'white')
            pop_up_window()


        for event in pygame.event.get():
            if current_screen == "input":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exam_date_input.rect.collidepoint(event.pos):
                        active_block = "exam"

                    elif wake_time_input.rect.collidepoint(event.pos):
                        active_block = "wake"

                    elif sleep_time_input.rect.collidepoint(event.pos):
                        active_block = "sleep"

                    elif study_time_input.rect.collidepoint(event.pos):
                        active_block = "study"

                    elif subject_input.rect.collidepoint(event.pos):
                        active_block = "subject"


                    else:
                        active_block =None

                    if generate_sched_button.check_click():
                        if check_date(exam_date):
                            current_screen = "pop up"
                        else:
                            current_screen = "schedule"


                elif event.type == pygame.KEYDOWN:
                    if active_block == "exam":
                        #exam_date_str = ""
                        if event.key == pygame.K_BACKSPACE:
                            exam_date = exam_date[:-1]
                            exam_date_str = exam_date_str[:-1]
                            #print(exam_date_str)
                        elif len(exam_date) >= 10:
                            continue
                        else:
                            if event.unicode.isnumeric() or event.unicode == '-':
                                exam_date += event.unicode
                                exam_date_str += event.unicode
                                #print(exam_date_str)
                            else:
                                continue
                            #exam_date += event.unicode

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

                    elif active_block == "study":
                        if event.key == pygame.K_BACKSPACE:
                            study_times= study_times[:-1]
                        else:
                            study_times += event.unicode

                    elif active_block == "subject":
                        if event.key == pygame.K_BACKSPACE:
                            subjects = subjects[:-1]
                        else:
                            subjects += event.unicode

            elif current_screen == "pop up":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pop_up_window_button.rect.collidepoint(event.pos):
                        current_screen = "input"

            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


        pygame.display.flip()

if __name__ == '__main__':
    main()
