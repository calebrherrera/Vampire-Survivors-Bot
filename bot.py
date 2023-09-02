# A bot that plays the game: Vampire Survivors
import time
import pyautogui
import keyboard
# import numpy as np
# import random
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

    def pressKey(self, key):
        keyboard.press_and_release(key)
        time.sleep(0.000001)
    
    
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


    # def move(self, direction):
        
    #     if (direction == "w"):
    #         print("Moving Up")
    #         pyautogui.keyDown('w')
    #         self.lastKey = 'w'
            
    #     elif (direction == "a"):
    #         print("Moving Left")
    #         pyautogui.keyDown('a')
    #         self.lastKey = 'a'
        
    #     elif (direction == "s"):
    #         print("Moving Down")
            
            
    #     elif (direction == "d"):
    #         print("Moving Right")
    #         pyautogui.keyDown('d')
    #         self.lastKey = 'd'
            
    #     else:
    #         print("Unknown direction")
            
        

    def walkInSquare(self,t):
        self.moveUp()
        time.sleep(t)
        self.moveRight()
        time.sleep(t)
        self.moveDown()
        time.sleep(t)
        self.moveLeft()
        time.sleep(t)
    
    

if __name__ == '__main__':
    time.sleep(7.5)
    
    bot = Bot()
    
    while (keyboard.is_pressed('q') == False):
        # bot.walkInCircle(0.00001)
        bot.moveUpLeft()
