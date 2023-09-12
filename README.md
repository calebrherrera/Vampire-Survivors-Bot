# Vampire-Survivors-Bot
 
This project aims to automate actions to play the game [Vampire Survivors](https://store.steampowered.com/app/1794680/Vampire_Survivors/)

Skills used in this project include:
- Python OOP
- Python mouse & keyboard interaction

### Current Status
- Bot upgrades the first available weapon when prompted.
- Bot revives or quits upon death.
- Character randomly walks

### Next Steps
- Make character walk towards chest if one is on screen
- Prioritize specific upgrades using priority queue
- Make character avoid enemies using motion planning algorithm

### Demo
If you'd like to try bot.py yourself, make sure you have python installed on your system. Then install the necessary modules using:
```
pip install pyautogui keyboard pywin32 opencv-python
```
Then once you've started Vampire Survivors and entered a game you can run the bot from the Vampire-Survivors-Bot directory using:
```
python bot.py
```