# A bot that plays the game: Vampire Survivors
import time
import pyautogui
import keyboard
import random
import win32api, win32con

class Bot():
    # Track last direciton chosen
    lastKey = '';
    # List of items to prioritize when upgrading
    # Ideally 6 'weapons' and 6 'relics' ordered from most to least important
    pick = ['whip', 'hollowheart'
            , 'duplicator', 'attractorb'
            , 'armor', 'garlic'
            , 'pummarola', 'runetracer'
            , 'crown']
    # List of weapons to 'banish' if no upgrades are available
    ban = ['pentagram', 'clover'
           , 'skullomaniac', 'firewand'
           , 'spellbinder', 'cross'
           , 'lightningring', 'santawater'
           , 'kingbible', 'knife']
    
    def __init__(self):
        print("Starting bot...")
    
    def click(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
    def move(self, direction, t):
        # print("Pressing " + direction)
        pyautogui.keyUp(self.lastKey)
        pyautogui.keyDown(direction)
        self.lastKey = direction
    
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
        if pyautogui.locateOnScreen('buttons/levelup.png', grayscale=True, confidence=0.8) != None:
            # print("Upgrade available.")
            return True
        return False
    
    def upgradeWeapon(self):
        time.sleep(0.5)
        for item in self.pick :
            path = "items\\" + item + ".png"
            # print("Looking for " + item)
            point = pyautogui.locateCenterOnScreen(path, grayscale=False, confidence=0.91, region=(615, 100, 1270 - 615, 900 - 100))
            if point != None:
                try:
                    self.click(point.x, point.y)
                    print("Upgraded " + item)
                    return
                except:
                    print("Couldn't click " + item)
            # else:
            #     print("Don't see " + item)
        
        self.reroll()
        self.banish()
        self.skip()
    
    def reroll(self):
        point = pyautogui.locateCenterOnScreen("buttons/reroll.png", grayscale=False, confidence=0.95)
        if point != None:
            self.click(point.x, point.y)
            time.sleep(0.5)
            self.upgradeWeapon()
        return False
    
    def banish(self):
        ban_button = pyautogui.locateCenterOnScreen("buttons/banish.png", grayscale=False, confidence=0.95)
        if ban_button != None:
            for item in self.ban:
                path = "items\\" + item + ".png"
                point = pyautogui.locateCenterOnScreen(path, grayscale=False, confidence=0.90, region=(615, 100, 1270 - 615, 900 - 100))
                if point != None:
                    try:
                        self.click(ban_button.x, ban_button.y)
                        time.sleep(0.5)
                        self.click(point.x, point.y)
                        print("Banished " + item)
                        return True
                    except:
                        print("Couldn't click " + item)
                # else:
                #     print("Don't see " + item)
        return False
    
    def skip(self):
        skip_button = pyautogui.locateCenterOnScreen("buttons/skip.png", grayscale=False, confidence=0.95)
        if skip_button != None:
            try:
                self.click(skip_button.x, skip_button.y)
                print("Skipped")
            except:
                print("Couldn't click skip")
            
    def chestFound(self):
        if pyautogui.locateOnScreen('items/chest.png', grayscale=True, confidence=0.6) != None:
            print("Chest found!!!")
            return True
        return False
    

if __name__ == '__main__':
    time.sleep(2)
    directions = ['w', 'a', 's', 'd']
    walk = 1
    
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
            bot.move(directions[random.randint(0,3)], walk)
        # bot.upgradeWeapon()
        time.sleep(0.0001)

    print("Exiting.")

