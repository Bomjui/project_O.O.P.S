import Text as txt
import os
import time
import Helpy as hlp
import curses
def OPPY_main(choice=False):
    starting_message = 0
    while True:
        if starting_message == 0:
            print(txt.Oopy_input_message[0])
            starting_message += 1
        while True:
            print("O.O.P.S[pl]/terminal >>> ", end="")
            time.sleep(0.5)
            player_input = input()
            save, result = "", ""
            if result not in txt.Oopy_help_list:
                for i in range(len(player_input)):
                    if player_input[i] == "(":
                        save = str(player_input[i+1:len(player_input)-1])
                        result = str(player_input[:i])
            if player_input == txt.Oopy_help_list[0]:
                break
            elif result in txt.Oopy_help_list:
                break
        if player_input == txt.Oopy_help_list[0]:
            print("Loading..", end="")
            hlp.animation_terminal(2, [".", ":", ";", ","], 0.3, True)
            os.system('cls')
            #for i in range(len(txt.Oopy_help_list)):
                #print(txt.Oopy_help_list[i], end=" ; ")

            #print("\n")
            #print("O.O.P.S[sys]/terminal >>> Список всех функций: ")
            back_main = curses.wrapper(
                lambda stdscr: hlp.history_printer(stdscr, f"O.O.P.S[sys]/terminal >>> Список всех функций: {str(txt.Oopy_help_list)}", 1))

        elif result == txt.Oopy_help_list[1]:
            print("Loading..", end="")
            hlp.animation_terminal(2, [".", ":", ";", ","], 0.3, True)
            os.system('cls')
            back_main = curses.wrapper(
                lambda stdscr: hlp.history_printer(stdscr, f"O.O.P.S[sys]/terminal >>> {save}",  1))
        elif result == txt.Oopy_help_list[2]:
            print(f"O.O.P.S[sys]/terminal >>> {save} = ", end="")
            a = input()
            print(f"O.O.P.S[sys]/terminal >>> {save} == {a}")
            time.sleep(2)



