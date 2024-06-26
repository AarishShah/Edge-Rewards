import pyautogui
import time
import random
import string
import os

def open_application(application_path):
    os.startfile(application_path)

def type_random_string_with_delay(interval, length, repetitions):
    for _ in range(repetitions):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        for char in random_string:
            pyautogui.typewrite(char)
            time.sleep(0.1)  # Slight delay between each character for realism
        pyautogui.press('enter')
        time.sleep(interval)

# Open Microsoft Edge
open_application('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')

# Give some time for Microsoft Edge to open
time.sleep(2)

# Type random 10-character strings with a delay of 30 seconds between each input
interval = 6 # check the delay in rewards and set accordingly
length = 3
repetitions = 33
type_random_string_with_delay(interval, length, repetitions)

# Close Microsoft Edge using os.system
os.system("TASKKILL /F /IM msedge.exe")
