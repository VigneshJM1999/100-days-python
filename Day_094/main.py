import time
import keyboard
import pyautogui
from PIL import ImageGrab

OBSTACLE_DETECTION_BOX = (460, 385, 600, 430)
OBSTACLE_THRESHOLD = 30

JUMP_KEY = 'space'
EXIT_KEY = 'q'
STARTUP_DELAY = 3


def jump():
    pyautogui.press(JUMP_KEY)
    print("Jump!")


def is_obstacle(pixel):
    return sum(pixel) > 350


def main():
    print(f"Starting Dino Bot in {STARTUP_DELAY} seconds...")
    print("Switch to the Chrome Dino game window now.")
    print(f"Press '{EXIT_KEY}' to quit.")
    time.sleep(STARTUP_DELAY)

    while True:
        if keyboard.is_pressed(EXIT_KEY):
            print("Exit key pressed. Shutting down the bot.")
            break

        screen = ImageGrab.grab(bbox=OBSTACLE_DETECTION_BOX)

        pixels = list(screen.getdata())

        obstacle_pixel_count = sum(1 for p in pixels if is_obstacle(p))

        if obstacle_pixel_count > OBSTACLE_THRESHOLD:
            jump()

        time.sleep(0.01)


if __name__ == "__main__":
    main()
