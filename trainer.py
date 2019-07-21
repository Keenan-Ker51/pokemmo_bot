# beggining of the training portion of a larger focus for a better bot, for free, and open source
#https://softwarerecs.stackexchange.com/questions/42664/python-gui-automation-library-for-simulating-user-interaction-in-apps
from pynput.keyboard import Key, Controller
import time
from random import randint
from image_reader import *
from numpy import matrix
import numpy as np


bot = Controller()

possible_pokemon = ("Pelipper", "Tentacruel", "Wingull", "Tentacool")
sup_eff = np.mean( matrix((89.74063800277392, 83.78918169209432, 69.36407766990291)))
print(sup_eff)
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
    gone_yet = False # set to True if you want to just spam, with no checking for sup_eff
    while True:
        bot.press('z')
        bot.release('z')
        print("                                     ",end='\r')
        print("Attacking", end='\r')
        if gone_yet == False:
            print("                                     ",end='\r')
            print("grabbing effectivness", end='\r')
            time.sleep(1)
            get_eff()
            print(np.mean( matrix((average_image_color('moves/scnd.png')))))
            if sup_eff- 0.5 <= np.mean( matrix((average_image_color("moves/frst.png")))) <= sup_eff+0.5:
                bot.press('z')
                bot.release('z')
                print("                                     ",end='\r')
                print("first move", end='\r')
                gone_yet = True

            elif sup_eff- 0.5 <= np.mean( matrix((average_image_color('moves/scnd.png'))))<= sup_eff+0.5:
                bot.press(Key.down)
                bot.release(Key.down)
                bot.press('z')
                bot.release('z')
                print("                                     ",end='\r')
                print("second move", end='\r')
                gone_yet = True

            elif sup_eff- 0.5 <= np.mean( matrix((average_image_color('moves/thrd.png'))))<= sup_eff+0.5:
                print("thrd mve: {}".format(np.mean( matrix((average_image_color('moves/scnd.png'))))))
                bot.press(Key.right)
                bot.release(Key.right)
                bot.press('z')
                bot.release('z')
                gone_yet = True

            elif sup_eff- 0.5 <= np.mean( matrix((average_image_color('moves/fourth.png'))))<= sup_eff+0.5:
                bot.press(Key.down)
                bot.release(Key.down)
                bot.press(Key.right)
                bot.release(Key.right)
                bot.press('z')
                bot.release('z')
                gone_yet = True
            else:
                bot.press('z')
                bot.release('z')
                print("                                     ",end='\r')
                print("default move", end='\r')
                gone_yet = True
        else:
            bot.press('z')
            bot.release('z')

        time.sleep(12)
        outside_battle("now")
        if return_avgs() <50:
            break


    ### DEPRIECIATED ###
    # for x in range(0,75):
    #     print("                                  ",end='\r')
    #     print("Spamming first attack: ",x,"/75", end='\r')
    #     bot.press('z')
    #     bot.release('z')
    #     time.sleep(0.2)

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
    outside_battle("start")
    for x in range(0,5):
        side_move()
    outside_battle("now")
    if return_avgs() >50:
        print("                                     ",end='\r')
        print("Waiting for battle", end='\r')
        time.sleep(10)
        attack_mode()
