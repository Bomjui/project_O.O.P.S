import Text as txt
import time
import Helpy as hlp
import curses

def oppenheimer(player_input, save, result):
    for i in range(len(player_input)):
        if player_input[i] == "(" and player_input[len(player_input)-1] == ")":
            save = str(player_input[i + 1:len(player_input) - 1])
            result = str(player_input[:i])
    if "(" not in player_input or ")" not in player_input:
        return "()", True
    else:
        return save, result

def OOPY_animation():
    print("O.O.P.S[pl]/terminal >>> Loading..", end="")
    hlp.animation_terminal(2, ("O", "O", "P", "Y"), 0.3, True)
def OPPY_main(choice=False):
    starting_message = 0
    while True:
        if starting_message == 0:
            print("O.O.P.S[sys]/terminal >>>", txt.Oopy_input_message[0])
            starting_message += 1
        while True:
            print("O.O.P.S[pl]/terminal >>> ", end="")
            time.sleep(0.5)
            save, result = "", ""
            player_input = input()
            if player_input not in txt.Oopy_help_list:
                save, result = oppenheimer(player_input, save, result)
                if result == True:
                    print(f"O.O.P.S[sys]/terminal >>> Syntaxis error you forgot paste {save} ")
                    break
            if player_input in txt.Oopy_help_list:
                break
            elif result in txt.Oopy_help_list:
                break
        if player_input == txt.Oopy_help_list[0]:
            OOPY_animation()
            back_main = curses.wrapper(
                lambda stdscr: hlp.history_printer(stdscr,
                            f"O.O.P.S[sys]/terminal >>> Список всех функций: {str(txt.Oopy_help_list)}", 1, True, False))

        elif result == txt.Oopy_help_list[1]:
            OOPY_animation()
            back_main = curses.wrapper(
                lambda stdscr: hlp.history_printer(stdscr, f"O.O.P.S[sys]/terminal >>> {save}",  1, True, False))
            print(f"O.O.P.S[sys]/terminal >>> {save}")
        elif result == txt.Oopy_help_list[2]:
            OOPY_animation()
            print(f"O.O.P.S[sys]/terminal >>> {save} = ", end="")
            player_input = input()
            save_printo, result = oppenheimer(player_input, "", "")
            if f"{result}" == "/printo":
                print(f"O.O.P.S[sys]/terminal >>> {save} == {save_printo}")
            else:
                print(f"O.O.P.S[sys]/terminal >>> Syntaxis error {result} <-- is not /printo")
            time.sleep(2)
        elif player_input == txt.Oopy_help_list[3]:
            OOPY_animation()
            back_main = curses.wrapper(
                lambda stdscr:
                hlp.OOPY_CHOICE_Function(stdscr, txt.Oopy_help_list, 0, 1))



