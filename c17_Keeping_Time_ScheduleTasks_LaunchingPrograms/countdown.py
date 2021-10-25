#! python3
# countdown.py - A simple countdown script.
"""
At a high level, here’s what your program will do: 
    1. Count down from 60.
    2. Play a sound file (alarm.wav) when the countdown reaches zero. 

This means your code will need to do the following:
    1. Pause for 1 second in between displaying each number in the countdown by calling time.sleep().
    2. Call subprocess.Popen() to open the sound file with the default application.

Open a new file editor tab and save it as countdown.py.
"""

import time, subprocess
from pathlib import Path

print(Path.cwd())
soundFilePath = f"{Path.cwd()}/c17_Keeping_Time_ScheduleTasks_LaunchingPrograms/alarm.wav"

print('\n'+'='*50+'\n')
print("Start counting down ...")
timeLeft = 3
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

# TODO: At the end of the countdown, play a sound file.
subprocess.Popen(['open', soundFilePath])
# subprocess.Popen(['open', 'alarm.wav'])
# subprocess.Popen(['python3', 'mutiTDWallPaper.py'])

# pathApp = "/System/Applications/Calculator.app/Contents/MacOS/Calculator"
# subprocess.Popen(pathApp)


print('\n'+'='*50+'\n')