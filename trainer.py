# beggining of the training portion of a larger focus for a better bot, for free, and open source
#https://softwarerecs.stackexchange.com/questions/42664/python-gui-automation-library-for-simulating-user-interaction-in-apps
from pynput.keyboard import Key, Controller
import time
from random import randint

bot = Controller()

def side_move():
    bot.press(Key.right)
    time.sleep(0.3)
    bot.release(Key.right)
    bot.press(Key.left)
    time.sleep(0.3)
    bot.release(Key.left)

def vert_move():
        bot.press(Key.up)
        time.sleep(0.4)
        bot.release(Key.up)
        bot.press(Key.down)
        time.sleep(0.45)
        bot.release(Key.down)
time.sleep(3)

def attack_mode():
    for x in range(0,75):
        print("                                  ",end='\r')
        print("Spamming first attack: ",x,"/75", end='\r')
        bot.press('z')
        bot.release('z')
        time.sleep(0.2)

def catch_mode():
    print("                                  ",end='\r')
    print("Waiting for player response", end='\r')
    time.sleep(4)
    print("                                  ",end='\r')
    print("leaving battle", end='\r')
    bot.press(Key.down)
    time.sleep(0.1)
    bot.release(Key.down)
    bot.press(Key.right)
    time.sleep(0.1)
    bot.release(Key.right)
    bot.press('z')
    bot.release('z')

while True:
    print("                                      ",end='\r')
    print("Moving PC",end='\r')

    for x in range(0,10):
        side_move()
    print("                                     ",end='\r')
    print("Waiting for battle", end='\r')
    time.sleep(7)
    catch_mode()
