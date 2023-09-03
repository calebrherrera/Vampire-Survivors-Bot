# A bot that plays the game: Vampire Survivors
import time
import pyautogui
import keyboard
import numpy as np
import random
import win32api, win32con

class Bot():
    lastKey = '';
    def __init__(self):
        print("Starting bot...")
        lastKey = ''
    
    def click(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
    def move(self, direction, t):
        print("Pressing " + direction)
        pyautogui.keyUp(self.lastKey)
        pyautogui.keyDown(direction)
        self.lastKey = direction
        # time.sleep(t)ssddadd
    
    def moveUp(self):
        print("Moving Up")
        pyautogui.keyUp(self.lastKey)
        pyautogui.keyDown('w')
        self.lastKey = 'w'

    def moveDown(self):
        print("Moving Down")
        pyautogui.keyUp(self.lastKey)
        pyautogui.keyDown('s')
        self.lastKey = 's'
        
    def moveLeft(self):
        print("Moving Left")
        pyautogui.keyUp(self.lastKey)
        pyautogui.keyDown('a')
        self.lastKey = 'a'

    def moveRight(self):
        print("Moving Right")
        pyautogui.keyUp(self.lastKey)
        pyautogui.keyDown('d')
        self.lastKey = 'd'
        
    def moveUpLeft(self):
        print("Moving Up Left")
        pyautogui.keyUp(self.lastKey)
        pyautogui.keyDown('w')
        pyautogui.keyDown('a')
        self.lastKey = ['w','a']
        
    def moveDownRight(self):
        print("Moving Up Left")
        pyautogui.keyUp(self.lastKey)
        pyautogui.keyDown('s')
        pyautogui.keyDown('d')
        self.lastKey = ['s','d']

    def walkInSquare(self,t):
        self.moveUp()
        time.sleep(t)
        self.moveRight()
        time.sleep(t)
        self.moveDown()
        time.sleep(t)
        self.moveLeft()
        time.sleep(t)
    
    def isDead(self):
        if (pyautogui.pixel(835, 745) == (209, 43, 12)):
            print("Bot died.")
            self.click(835, 745)
            return True
        elif (pyautogui.pixel(845, 925) == (62, 179, 90)):
            print("Reviving")
            self.click(845, 925)
        return False
    
    def tryRevive(self):
        self.click(835, 745)
    
    def checkRevive(self):
        if pyautogui.locateOnScreen('buttons/revive.png', grayscale=True, confidence=0.8) != None:
            button = pyautogui.locateCenterOnScreen('buttons/revive.png', grayscale=True)
            print("Reviving")
            self.click(button.x, button.y)   
    
    def upgradeAvailable(self):
        if (pyautogui.pixel(935, 325) == (133, 133, 131)):
            print("Upgrade available.")
            return True
        return False
    
    def upgradeWeapon(self):
        self.click(935, 325)
        print("Upgrade chosen.")
    
    def chestFound(self):
        if pyautogui.locateOnScreen('items/chest.png', grayscale=True, confidence=0.8) != None:
            print("Chest found!!!")
            return True
        return False
    

if __name__ == '__main__':
    time.sleep(2)
    directions = ['w', 'a', 's', 'd']
    max_walk = 1
    
    bot = Bot()
    
    while (keyboard.is_pressed('q') == False):
        
        if bot.upgradeAvailable():
            # Check if upgrade available
            bot.upgradeWeapon()
        elif bot.isDead():
            # Check if character died
            break
        elif bot.chestFound():
            # Check if chest is on screen
            continue
        else:
            bot.move(directions[random.randint(0,3)], random.randrange(0,max_walk))
        
        time.sleep(0.0001)

    print("Exiting.")

