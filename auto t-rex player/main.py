import pyautogui
from PIL import Image, ImageGrab
import time


def click(key):
    pyautogui.keyDown(key)
    return


def isCollision(data):
    # Check colison for birds
    # for i in range(268, 298):
    #     for j in range(265, 312):
    #         if data[i, j] < 171:
    #             click("down")
    #             return
    # Check colison for cactus

    for i in range(276, 401):
        for j in range(315, 345):
            if data[i, j] < 100:
                click("up")
                return
    return


if __name__ == "__main__":
    # time.sleep(5)
    click('up')


while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    isCollision(data)

    # # Draw the rectangle for cactus
    # for i in range(255, 285):
    #     for j in range(265, 312):
    #          data[i, j] = 0
    #
    # # # Draw the rectangle for birds
    # for i in range(255, 345):
    #     for j in range(315, 345):
    #         data[i, j] = 171
    #
    # image.show()
    # break
