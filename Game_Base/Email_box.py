from random import choice
import time
import os
import Text as txt
import Helpy as hlp
import curses

def message(number, save_message):
    arr = []
    if number == 0:
        for i in range(0, 500):
            arr.append(i)
    time.sleep(1)
    if number == 1:
        message_main = curses.wrapper(lambda stdscr: hlp.main(stdscr, [save_message, "[X]EXIT"], 0, "Messager", 0, 1, True))
        if message_main == "[X]EXIT":
            return save_message, number
    elif number == 0:
        if choice(arr) <= 250:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_safe))
        elif choice(arr) <= 500:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_safe))
        message_main = curses.wrapper(lambda stdscr: hlp.main(stdscr, [save_message, "[X]EXIT"], 0, "Messager", 0, 1, True))
        if message_main == "[X]EXIT":
            return save_message, number

def message_see(number):
    if number == 1:
        return True
    elif number == 0:
        return False