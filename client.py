import time
import pyautogui
import keyboard
import win32api

def spin(x, y):
    win32api.SetCursorPos((x, y - 100))
    time.sleep(0.01)
    win32api.SetCursorPos((x + 100, y))
    time.sleep(0.01)
    win32api.SetCursorPos((x, y + 100))
    time.sleep(0.01)
    win32api.SetCursorPos((x - 100, y))
    time.sleep(0.01)


def main():
    screen_x, screen_y = pyautogui.size()
    print(f'---{screen_y}p detected---')
    print('To spin just press space')
    while True:
        while keyboard.is_pressed('space'):
            spin(int(screen_x/2), int(screen_y/2))

if __name__ == "__main__":
    main()
