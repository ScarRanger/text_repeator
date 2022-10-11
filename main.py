import pyautogui
import time
time.sleep(4) #4 secs delay to switch windows
count = 0
while count <=100: #Number of time to be repeated
    pyautogui.typewrite("Hello "+str(count)) #text to be repeated
    pyautogui.press("enter")
    count += 1
