from random import choice
import time
import Text as txt
import Helpy as hlp
import curses

def message(number, save_message, place, timer=0):
    arr = []
    message_main = ""
    time.sleep(1)
    if number == 1:
        message_main = curses.wrapper(lambda stdscr:
                    hlp.main(stdscr, ["[!]Bring the soldiers in place", "[<]BACK", "[X]EXIT"], 0,
                             f"----[O.O.P.S.Y]---- in [{place}]",
                             0, 2, True, False, timer, True, save_message))
    elif number == 0:
        arr = choice(range(0, 1000))
        if arr <= txt.difficult[0]:
            save_message = "Nothing"
        elif arr <= txt.difficult[1]:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_safe))
        elif arr <= txt.difficult[2]:
            number += 1
            save_message = choice(hlp.for_i_help(txt.messages_str))
        elif arr <= txt.difficult[3]:
            save_message = choice(hlp.for_i_help(txt.messages_ocs))
        elif arr == txt.difficult[4]:
            save_message = choice(hlp.for_i_help(txt.messages_00PS))
        message_main = curses.wrapper(lambda stdscr:
                        hlp.main(stdscr, ["[!]Bring the soldiers in place", "[<]BACK", "[X]EXIT"], 0,
                                 f"----[O.O.P.S.Y]---- in [{place}]",
                                 0, 2, True, False, timer, True, save_message))
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