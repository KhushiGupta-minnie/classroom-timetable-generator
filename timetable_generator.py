# Classroom Timetable Generator

days_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Taking input
days = int(input("Enter number of days: "))
periods_per_day = int(input("Enter periods per day: "))

# Input validation
if days <= 0 or days > 6 or periods_per_day <= 0:
    print("Error: Invalid days or periods.")
    exit()

n = int(input("Enter number of subjects: "))

if n <= 0:
    print("Error: At least one subject is required.")
    exit()

# Dictionary to store subjects and periods
remaining = {}

for i in range(n):
    subject = input("Enter subject name: ")
    periods = int(input("Enter periods for " + subject + ": "))

    if subject in remaining or periods <= 0:
        print("Error: Invalid subject or periods.")
        exit()

    remaining[subject] = periods

# Check total periods
total_periods = sum(remaining.values())
total_slots = days * periods_per_day

if total_periods != total_slots:
    print("Error: Total weekly periods (" + str(total_periods) +
          ") must equal available slots (" + str(total_slots) + ").")
    exit()

# Check daily limit
for subject in remaining:
    if remaining[subject] > days * 2:
        print("Error: " + subject +
              " needs more than 2 periods per day.")
        exit()

# Generate timetable
timetable = []

for day in range(days):

    daily_count = {}
    daily_schedule = []

    for period in range(periods_per_day):

        # Find subjects having remaining periods
        available = [
            subject for subject in remaining
            if remaining[subject] > 0
            and daily_count.get(subject, 0) < 2
        ]

        if not available:
            print("Error: Timetable cannot be generated.")
            exit()

        # Select subject with maximum remaining periods
        selected = max(available, key=lambda x: remaining[x])

        daily_schedule.append(selected)

        remaining[selected] -= 1

        daily_count[selected] = daily_count.get(selected, 0) + 1

    timetable.append(daily_schedule)

# Print timetable
print("\n========== WEEKLY TIMETABLE ==========")

for i in range(days):
    print(days_name[i] + ": " + ", ".join(timetable[i]))