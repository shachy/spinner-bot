import time

import pyautogui
import keyboard
import win32api


def spin_fhd():
    win32api.SetCursorPos((960, 440))
    time.sleep(0.01)
    win32api.SetCursorPos((1060, 540))
    time.sleep(0.01)
    win32api.SetCursorPos((960, 640))
    time.sleep(0.01)
    win32api.SetCursorPos((860, 540))
    time.sleep(0.01)


def spin_hd():
    win32api.SetCursorPos((640, 260))
    time.sleep(0.01)
    win32api.SetCursorPos((740, 360))
    time.sleep(0.01)
    win32api.SetCursorPos((640, 460))
    time.sleep(0.01)
    win32api.SetCursorPos((540, 360))
    time.sleep(0.01)


def spin_2k():
    win32api.SetCursorPos((1280, 620))
    time.sleep(0.01)
    win32api.SetCursorPos((1380, 720))
    time.sleep(0.01)
    win32api.SetCursorPos((1280, 820))
    time.sleep(0.01)
    win32api.SetCursorPos((1180, 720))
    time.sleep(0.01)


def spin_4k():
    win32api.SetCursorPos((1920, 980))
    time.sleep(0.01)
    win32api.SetCursorPos((2020, 1080))
    time.sleep(0.01)
    win32api.SetCursorPos((1920, 1280))
    time.sleep(0.01)
    win32api.SetCursorPos((1820, 1080))
    time.sleep(0.01)


def main():
    screen_size = pyautogui.size()

    if screen_size[0] == 1920 and screen_size[1] == 1080:
        print('--1080p detected--')
        print('To spin just press space')
        while True:
            while keyboard.is_pressed('space'):
                spin_fhd()

    elif screen_size[0] == 1280 and screen_size[1] == 720:
        print('--720p detected--')
        print('To spin just press space')
        while True:
            while keyboard.is_pressed('space'):
                spin_hd()

    elif screen_size[0] == 2560 and screen_size[1] == 1440:
        print('--1440p detected--')
        print('To spin just press space')
        while True:
            while keyboard.is_pressed('space'):
                spin_2k()

    elif screen_size[0] == 3840 and screen_size[1] == 2160:
        print('--2160p detected--')
        print('To spin just press space')
        while True:
            while keyboard.is_pressed('space'):
                spin_4k()


main()
