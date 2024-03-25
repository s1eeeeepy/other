import pyautogui
from pynput import keyboard
from time import sleep
import sys

my_kb = keyboard.Controller()


def on_release(key):
    global start
    if key == keyboard.Key.esc:
        start = False


phrases = ["start", "go", "g", "y", "yes"]

listener = keyboard.Listener(on_release=on_release)
listener.start()


def main():
    start = input("Type 'go' to start digging!\n").lower()
    print("Estimating digging time: 30-40 min\nTake a nap <3\nPress 'Esc' to exit!")
    sleep(4)
    for i in range(5)[::-1]:
        print(f"Script will start in {i+1}... Tab into the game!")
        print("Press 'Esc' button to exit!")
        sleep(1)
    print("Digging begins now!")
    while start in phrases:
        pyautogui.mouseDown()
        sleep(0.1)
        pyautogui.mouseUp()
        my_kb.press("s")
        sleep(0.1)
        my_kb.release("s")
        sleep(0.1)

    print("Job is Done, have a nice one!")
    sleep(5)
    sys.exit()


if __name__ == "__main__":
    main()
