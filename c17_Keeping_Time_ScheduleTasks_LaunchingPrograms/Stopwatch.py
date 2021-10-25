#! Python3
# Stopwatch.py
# PROJECT: SUPER STOPWATCH
"""
Project Task: To write a simple stopwatch program in Python.

Overall, the program does the following:
    1. Track the amount of time elapsed between presses of the ENTER key, with 
       each key press starting a new “lap” on the timer.
    2. Print the lap number, total time, and lap time.

So the code will need to do the following:
    1. Find the current time by calling time.time() and store it as a timestamp 
       at the start of the program, as well as at the start of each lap.
    2. Keep a lap counter and increment it every time the user presses ENTER.
    3. Calculate the elapsed time by subtracting timestamps.
    4. Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.

Open a new file editor tab and save it as stopwatch.py.
"""

import time, sys

print("\n")
print(" CHAPTER 17 PROJECT: SUPER STOPWATCH ".center(100, '='))
print("== 1. To start the Stopwatch, please press any key.".ljust(97),"==")
print("== 2. To quit Stopwatch, please press 'Ctrol+C' keys.".ljust(97),"==")
print('='*100)
try:
    input()
    start_time = end_lap_time = time.time()
    lap_count = 0
    format_space = 20

    print("Stopwatch is running ... \n( press any key to start a new time lap, or 'Ctrol+C' to quit Stopwatch program. )")
    print("\n", "lap number".rjust(format_space), "total time".rjust(format_space), "lap time".rjust(format_space))

    while True:
        input()
        start_lap_time = time.time()
        total_time = round(start_lap_time - start_time, 2)
        lap_time = round(start_lap_time - end_lap_time, 2)
        end_lap_time = start_lap_time
        lap_count += 1
        print(f"lap #{lap_count}:".rjust(format_space), end="")
        print(f"{total_time}s".rjust(format_space), end="")
        print(f"{lap_time}s".rjust(format_space), end="")
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print("\n\nQuitting Stopwatch program! BYE!\n")
    sys.exit()