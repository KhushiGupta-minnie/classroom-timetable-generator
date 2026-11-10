# Classroom Timetable Generator

A Python 3 project that generates a weekly classroom timetable automatically.

## Project Description

This project generates a weekly timetable based on the number of days, periods per day, subjects, and their required periods.

It uses a greedy scheduling approach to fill the timetable.

## Features

- Generates a weekly classroom timetable.
- Takes input from the user.
- Ensures total periods equal available slots.
- Allows a maximum of 2 periods per subject per day.
- Selects the subject with the most remaining periods.
- Resolves ties using the order in which subjects were entered.

## Technologies Used

- Python 3
- Lists
- Dictionaries
- Conditional Statements
- Loops
- Scheduling Algorithm

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python timetable_generator.py
```

5. Enter the required inputs.

## Example Output

```text
========== WEEKLY TIMETABLE ==========

Mon: programming, english
Tue: programming, english
```

## Constraints

- Total weekly periods must equal total available slots.
- A subject can have at most 2 periods per day.
- The subject with the most remaining periods is selected first.
- Ties are resolved by input order.

## Author

Khushi Kumari

B.Tech CSE Core

## Project Report
[Download Project Report (PDF)](Classroom%20Timetable%20Generator%20-%20Project%20Report.pdf)




## Test Case Screenshots

1. [Test Case 1 Output](test%20case%201%20-%20screenshot.png)

2. [Test Case 2 Output](test%20case%202%20-%20screenshot.png)

3. [Test Case 3(a) Output](test%20case%203%20(a)%20-%20screenshot.png)

4. [Test Case 3(b) Output](test%20case%203%20(b)%20-%20screenshot.png)

5. [Test Case 4 Output](test%20case%204%20-%20screenshot.png)

