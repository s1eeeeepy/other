import pyautogui
import time


def hold():
    time.sleep(3)
    count = 0
    while count < 10000:
        pyautogui.press("e")
        count += 1


hold()
