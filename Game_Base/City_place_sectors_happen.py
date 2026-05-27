from random import choice
import time
import Text as txt
import Helpy as hlp
import curses

def message(number, save_message, place):
    arr = []
    if number == 0:
        for i in range(0, 500):
            arr.append(i)
    time.sleep(1)
    if number == 1:
        message_main = curses.wrapper(lambda stdscr:
                    hlp.main(stdscr, [save_message, "[!]Bring the soldiers in place", "[<]BACK", "[X]EXIT"], 0,
                             f"----[O.O.P.S.Y]---- in [{place}]",
                             0, 1, True), )
        if message_main == "[X]EXIT":
            return save_message, number, True
        elif message_main == "[X]EXIT":
            return save_message, number, False
        else:
            return save_message, number, "I always come BACK!"
    elif number == 0:
        if choice(arr) <= 250:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_safe))
        elif choice(arr) <= 500:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_safe))
        message_main = curses.wrapper(lambda stdscr:
                        hlp.main(stdscr, [save_message, "[!]Bring the soldiers in place", "[<]BACK", "[X]EXIT"], 0, f"----[O.O.P.S.Y]---- in [{place}]",
                                 0, 1, True))
        if message_main == "[X]EXIT":
            return save_message, number, True
        elif message_main == "[X]EXIT":
            return save_message, number, False
        else:
            return save_message, number, "I always come BACK!"

def message_see(number):
    if number == 1:
        return True
    elif number == 0:
        return False