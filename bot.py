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
    
    def checkRevive(self):
        if pyautogui.locateOnScreen('images/revive.png', grayscale=True, confidence=0.8) != None:
            button = pyautogui.locateCenterOnScreen('images/revive.png', grayscale=True)
            print("Reviving")
            self.click(button.x, button.y)   
    

if __name__ == '__main__':
    time.sleep(2)
    
    bot = Bot()
    
    while (keyboard.is_pressed('q') == False):
        # bot.walkInCircle(0.00001)
        bot.checkRevive()
        time.sleep(1)
        # bot.moveUpLeft()
        # time.sleep(1)
        # bot.moveDownRight()
        # time.sleep(1)
    
    print("Bot died or user exited")

