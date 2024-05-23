#! python3
# countdown.py - A simple countdown script.
import time, subprocess
u timeLeft = 60
while timeLeft > 0:
v print(timeLeft, end='')
w time.sleep(1)
x timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)