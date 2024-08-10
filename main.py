import pyautogui
import time

time.sleep(1)

while True:
    x, y = pyautogui.position()
    pyautogui.click(x, y)
    time.sleep(0.3)
