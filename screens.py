import pygame
import datetime

pygame.init()
pygame.key.set_repeat(300, 200)

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 35

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Study Scheduler")
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, 50)
pop_up_font = pygame.font.Font(None, 25)
date_info_font = pygame.font.Font(None, 30)
blocks_info_font = pygame.font.Font(None, 22)
pomodoro_sentence_font = pygame.font.Font(None, 20)

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
        """
        Draws the button on the screen with the words and in the specific location on the screen.
        """
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
        """
        Returns True or False depending on if the rectangle of the button was clicked.
        """
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = self.rect
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class DayBlock:
    def __init__(self, date_str, times, words_per_time, x_start = 15, y_start = 80):
        self.x_start = x_start
        self.y_start = y_start
        self.date_str = date_str
        self.times = times
        self.color = WHITE
        self.words = words_per_time

    def draw(self):
        """
        Draws each individual DayBlock on the screen with its schedule details. DayBlock is drawn in the proper location by adjusting the x_start and y_start per DayBlock.
        """
        rect = pygame.Rect(self.x_start, self.y_start, 250, 250)
        pygame.draw.rect(screen, WHITE, rect)

        date_font = date_info_font.render(self.date_str, True, BLACK)
        screen.blit(date_font, (self.x_start + 10, self.y_start + 10))

        y_offset = self.y_start + 45
        for ind, (time, phrase) in enumerate(zip(self.times, self.words)):
            time_font = blocks_info_font.render(f"{time}:", True, BLACK)
            screen.blit(time_font, (self.x_start + 10, y_offset))
            words = phrase.split(" ")
            line = ""
            line_num = 0
            for word in words:
                check_line = line + word + " "
                text = pomodoro_sentence_font.render(check_line, True, BLACK)
                if text.get_width() < 180:
                    line = check_line
                else:
                    printed_line = pomodoro_sentence_font.render(line, True, BLACK)
                    screen.blit(printed_line, (self.x_start + 58, y_offset + 1 + line_num * 20))
                    line = word + " "
                    line_num += 1
            printed_line = pomodoro_sentence_font.render(line, True, BLACK)
            screen.blit(printed_line, (self.x_start + 60, y_offset + 1 + line_num * 20))
            y_offset += (line_num + 1) * 20 + 10

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
    screen.blit(exam_date_label, (15, 160))

    wake_time_label = font.render("Wake Up Time (HH:MM):", True, BLACK)
    screen.blit(wake_time_label, (45, 215))

    sleep_time_label = font.render("Sleep Time (HH:MM):", True, BLACK)
    screen.blit(sleep_time_label, (80, 270))

    study_time_label = font.render("Study Times (HH:MM):", True, BLACK)
    screen.blit(study_time_label, (62, 325))

    subject_label = font.render("Subjects:", True, BLACK)
    screen.blit(subject_label, (210, 380))

def draw_schedule_screen(exam_date: str, times: list, words_per_time: list):
    """
    Draws the schedule screen based on the provided exam date.

    This function clears the screen and displays "Your Schedule" title, generates a list of dates from today up to the exam date.
    It creates and draws DayBlock objects for each date, organizing them into two rows: the first 3 days on the top row and the next three days on the second row.

    Args:
    exam_date (str): In 'YYYY-MM-DD' format.
    times (list): the times that are going to be displayed on the block
    words_per_time (list): the phrase associated with each time
    """
    screen.fill("darkslategray4")
    title = title_font.render("Your Schedule", True, WHITE)
    screen.blit(title, (275, 40))

    curr_date = datetime.date.today()
    exam_date_obj = datetime.date(int(exam_date[0:4]), int(exam_date[5:7]), int(exam_date[8:]))
    days_till = (exam_date_obj - curr_date).days
    dates = []
    for days_past in range(days_till+1):
        date_obj = curr_date + datetime.timedelta(days=days_past)
        date_str = date_obj.strftime('%Y-%m-%d')
        dates.append(date_str)

    x_pos = 10
    for day,date in enumerate(dates):
        if day < 3:
            box = DayBlock(date, times, words_per_time, x_pos)
            box.draw()
            x_pos += 265

        if 3 <= day <= 5:
            if day == 3:
                x_pos = 10
                y_pos = 340
            box = DayBlock(date, times, words_per_time, x_pos, y_pos)
            box.draw()
            x_pos += 265

def pop_up_window():
    """
    Displays a pop-up window to handle invalid exam date inputs.

    The function clears the screen and shows a message prompting the user to select an exam date within 6 days if their original input is too far in the future. It creates a white rectangle as the pop-up box and renders a wanring message inside it.
    """
    screen.fill("darkslategray4")

    message = pop_up_font.render("You have plenty of time! Choose a date within 6 days!", True, BLACK)
    pop_up = pygame.Rect(180, 250, 450, 60)
    pygame.draw.rect(screen, WHITE, pop_up)
    screen.blit(message, (185, 270))

def check_date(exam_date):
    """
    Validates whether the date is in the future and within 6 days of the current date.
    Takes in the exam_date string from the user input on the input screen. Returns True or False depending on validity of date.
    """
    if exam_date == '':
        return True
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
    times = []

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
            draw_schedule_screen(exam_date, times, words_per_time)

        elif current_screen == "pop up":
            pop_up_window_button = Button("None", 180, 250, 450, 60, True, 'white')
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
                            times.extend([wake_time, study_times, sleep_time])
                            if len(subjects) > 1:
                                subjects = subjects.split(",")
                                subjects = ' and '.join(subjects)

                            words_per_time = ["Wake up!", f"Study {subjects} in eight 30 minute increments with 5 minute breaks in between, and a 15 minute break after four sessions.",
                                              "Sleep!"]
                            current_screen = "schedule"

                elif event.type == pygame.KEYDOWN:
                    if active_block == "exam":
                        if event.key == pygame.K_BACKSPACE:
                            exam_date = exam_date[:-1]
                            exam_date_str = exam_date_str[:-1]
                        elif len(exam_date) >= 10:
                            continue
                        else:
                            if event.unicode.isnumeric() or event.unicode == '-':
                                exam_date += event.unicode
                                exam_date_str += event.unicode
                            else:
                                continue

                    elif active_block == "wake":
                        if event.key == pygame.K_BACKSPACE:
                            wake_time = wake_time[:-1]
                        elif len(wake_time) >= 5:
                            continue
                        else:
                            if event.unicode.isnumeric() or event.unicode == ":":
                                wake_time += event.unicode
                            else:
                                continue

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