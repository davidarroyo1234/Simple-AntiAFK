import random
import pyautogui
import time

keys = ["w", "a", "s", "d"]


class term_color:
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def mode_selection():
    available_selection = [1, 2]
    while True:
        try:
            selection = int(input(
                "Select your anti-AFK mode\n" +
                "[1] Social (Teams,Skype,Discord) This mode moves the mouse every interval you specified. \n" +
                "[2] Games (Minecraft,CSGO....) This mode moves the mouse and presses movement keys (WASD) every interval you specified.\n"
                ">>> "))
            if available_selection.__contains__(selection):
                return selection
            else:
                raise ValueError
        except ValueError:
            print(f"{term_color.FAIL}Chose a valid number from the list{term_color.ENDC}")


def seconds_interval():
    while True:
        try:
            second_selection = int(input("Select every how many seconds it will repeat >>> "))
            if isinstance(second_selection, int):
                return second_selection
            else:
                raise ValueError
        except ValueError:
            print(f"{term_color.FAIL}Value must be a number{term_color.ENDC}")


def move_mouse():
    current_mouse_x, current_mouse_y = pyautogui.position()
    pyautogui.moveTo(current_mouse_x - 1, current_mouse_y - 1)


def main():
    try:
        mode = mode_selection()
        seconds_to_repeat = seconds_interval()
        while True:
            if mode == 1:
                move_mouse()
            elif mode == 2:
                move_mouse()
                rand = random.randint(0, len(keys) - 1)
                press_and_depress_with_delay(keys[rand], 0.5)
            time.sleep(seconds_to_repeat)
    except KeyboardInterrupt:
        pass


def press_and_depress_with_delay(key, sleep):
    pyautogui.keyDown(key)
    time.sleep(sleep)
    pyautogui.keyUp(key)


if __name__ == "__main__":
    main()
