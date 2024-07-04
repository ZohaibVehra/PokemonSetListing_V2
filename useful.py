import pyautogui
import time


def fullscrollUp():
    pyautogui.press('home')


def fullscrollDown():
    pyautogui.press('end')


def zoomInF():
    with pyautogui.hold('ctrl'):
        pyautogui.press('+', presses=11)

def zoomOutF():
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=9)


def moveClick(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()