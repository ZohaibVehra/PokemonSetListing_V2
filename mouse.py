import pyautogui
import time
from useful import *


def loc():
    time.sleep(0.5)

    x = pyautogui.position()[0]
    y = pyautogui.position()[1]

    print(x, ',', y)

    time.sleep(1)

    x = pyautogui.position()[0]
    y = pyautogui.position()[1]

    print(x, ',', y)

    time.sleep(1)

    x = pyautogui.position()[0]
    y = pyautogui.position()[1]

    print(x, ',', y)

time.sleep(0.5)

loc()
