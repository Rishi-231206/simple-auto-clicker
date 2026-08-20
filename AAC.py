import pyautogui
import time


def perform_task():

    x, y = 1710, 1010
    pyautogui.moveTo(x, y)

    pyautogui.click()

    wait_time = 70

    time.sleep(wait_time)

    x, y = 1710, 1010
    pyautogui.moveTo(x, y)

    pyautogui.click()
    pyautogui.click()

    time.sleep(5)

    pyautogui.click() 

while True:
    perform_task()
    time.sleep(5)


