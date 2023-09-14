import time
import pyautogui

while True:
    path = "items\\kingbible.png"
    point = pyautogui.locateCenterOnScreen(path, grayscale=True, confidence=0.90, region=(615, 100, 675, 900))
    print("Looking....")
    if (point != None):
        print("I see item at:")
        print(point)
        pyautogui.moveTo(point.x, point.y)
        break
    time.sleep(2)

# im = pyautogui.screenshot(region=(615, 100, 675, 900))
# im.save(r".\\visible.png")