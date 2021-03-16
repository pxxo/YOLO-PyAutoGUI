import pyautogui
import time

pyautogui.FAILESAFE = True
# size
size = pyautogui.size()
posx = size[0] / 2 * -1
posy = size[1] / 2
# click
# pyautogui.click(x=-960, y=540, duration=5)
pyautogui.click(x=posx, y=posy)
counter = 0