from random import choice
import time
import os
import Text as txt
import Helpy as hlp

def message(number, save_message):
    arr = []
    if number == 0:
        for i in range(0, 100):
            arr.append(i)
    time.sleep(1)
    print("Your messages:")
    time.sleep(1)

    if number == 1:
        print(save_message)
    elif number == 0:
        if choice(arr) <= 250:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_str))
        elif choice(arr) <= 500:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_safe))
        print(save_message)
    while True:
        task_choosing = int(input("Yes[1]/No[2]\nEnter 0 for exit::"))
        os.system('cls')
        if task_choosing == 0:
            return save_message, number

def message_see(number):
    if number == 1:
        return True
    elif number == 0:
        return False