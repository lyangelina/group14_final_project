import math
import datetime
import calendar

"""
Goal: Generate study schedule according to user preferences

Schedule generator inputs:
- Current date
- Exam date
- User wake-up and sleep time
- Desired number/length of study breaks
- Max. amount of study hours per day

Generated schedule output:
- Day-by-day schedule w/ study start/end times
- Allotted breaks

Not worrying about user input rn
"""

curr_date = datetime.date.today()
exam_date = datetime.date(2025, 4, 20) # Sample value
days = (exam_date - curr_date).days # days able to study

max_hours = 8 # Sample val
wake_time = 6 # 6AM, ints for now
sleep_time = 9 # 9 PM
start_time = 1 #PM
end_time = 4 #PM

class_time_start = 8 #AM
class_time_end = 12 #PM
exam_subj = "Math"
study_len = 30 # in minutes, integer

if study_len <= 30:
    break_len = 5
elif study_len <= 60:
    break_len = 10
elif study_len <= 120:
    break_len = 20
else:
    break_len = 30

# study_total = sleep_time - wake_time #hours available -> convert to minutes(??)
study_total = end_time - start_time #study block during day
study_total *=60

num_study_session = study_total//study_len
num_breaks = num_study_session - 1

#Sample idea of what an output schedule may look like
print(f"Wake up: {wake_time}AM")
print(f"Study {exam_subj}: {start_time}PM - {end_time}PM - {num_study_session} sessions of {study_len} minute with {break_len} minute breaks inbetween each session")
print(f"Free time: {end_time}PM - {sleep_time}PM")
print(f"Sleep: {sleep_time}PM")

def generate_schedule(exam_date: datetime.date):
    return None

print(curr_date.weekday())
print("days:", days)