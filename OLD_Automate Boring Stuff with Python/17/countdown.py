#! python3
# countdown.py - A simple countdown script.

import time, subprocess, os

print('\n'+'='*50+'\n')
timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# TODO: At the end of the countdown, play a sound file.
subprocess.Popen(['open', 'alarm.wav'])
subprocess.Popen(['python3', 'mutiTDWallPaper.py'])

# pathApp = "/System/Applications/Calculator.app/Contents/MacOS/Calculator"
# subprocess.Popen(pathApp)


print('\n'+'='*50+'\n')