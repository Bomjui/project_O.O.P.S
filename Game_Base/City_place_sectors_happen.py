from random import choice
import time
import Text as txt
import Helpy as hlp
import curses

def message(number, save_message, place, timer=0):
    arr = []
    if number == 0:
        arr = choice(range(0, 500))
    time.sleep(1)
    if number == 1:
        message_main = curses.wrapper(lambda stdscr:
                    hlp.main(stdscr, ["[!]Bring the soldiers in place", "[<]BACK", "[X]EXIT"], 0,
                             f"----[O.O.P.S.Y]---- in [{place}]\n{save_message}",
                             0, 2, True, False, timer), )
        if message_main == "[X]EXIT":
            return save_message, number, True
        elif message_main == "[<]BACK":
            return save_message, number, False
        else:
            return save_message, number, "I always come BACK!"
    elif number == 0:
        if arr <= 250:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_safe))
        elif arr <= 500:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_safe))
        message_main = curses.wrapper(lambda stdscr:
                        hlp.main(stdscr, ["[!]Bring the soldiers in place", "[<]BACK", "[X]EXIT"], 0,
                                 f"----[O.O.P.S.Y]---- in [{place}]\n{save_message}",
                                 0, 2, True, False, timer))
        if message_main == "[X]EXIT":
            return save_message, number, True
        elif message_main == "[<]BACK":
            return save_message, number, False
        else:
            return save_message, number, "I always come BACK!"

def message_see(number):
    if number == 1:
        return True
    elif number == 0:
        return False