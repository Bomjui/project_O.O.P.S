import asyncio

import Text as txt
import time
import Helpy as hlp
import curses
count = 0
async def oppenheimer(stdcsr, player_input, save, result):
    try:
        not_symbols = player_input.index("(")
        if player_input[:not_symbols] in txt.Oopy_help_list:
            if player_input[not_symbols] == "(" and player_input[len(player_input)-1] == ")":
                save = player_input[not_symbols + 1:len(player_input) - 1]
                result = player_input[:not_symbols]
            if "(" not in player_input or ")" not in player_input:
                return "()", True
            return save, result
        else:
            print("O.O.P.S[sys]/terminal >>> This is don't function")
            return False, False
    except ValueError:
        print("O.O.P.S[sys]/terminal >>> This is don't function")
        return False, False

async def OOPY_animation(stdscr):
    await asyncio.sleep(1)
    await hlp.animation_terminal(stdscr, 2, ("O", "O", "P", "Y"), 0.3, "O.O.P.S[pl]/terminal >>> Loading..", True)
async def OPPY_main(stdscr):
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
            await OOPY_animation(stdscr)
            print(f"O.O.P.S[sys]/terminal >>> Список всех функций: {str(txt.Oopy_help_list)}")

        elif result == txt.Oopy_help_list[1]:
            await OOPY_animation(stdscr)
            print(f"O.O.P.S[sys]/terminal >>> {save}")
        elif result == txt.Oopy_help_list[2]:
            await OOPY_animation()
            print(f"O.O.P.S[sys]/terminal >>> {save} = ", end="")
            player_input = input()
            save_printo, result = oppenheimer(player_input, "", "")
            if f"{result}" == "/printo":
                print(f"O.O.P.S[sys]/terminal >>> {save} == {save_printo}")
            else:
                print(f"O.O.P.S[sys]/terminal >>> Syntaxis error {result} <-- is not /printo")
        elif player_input == txt.Oopy_help_list[3]:
            await OOPY_animation(stdscr)
            back_main = curses.wrapper(
                lambda stdscr:
                hlp.OOPY_CHOICE_Function(stdscr, txt.Oopy_help_list, 0, 1,
                True, "O.O.P.S[sys]/terminal >>> Function list <<<"))
            if back_main == txt.Oopy_help_list[0]:
                print(f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[0]} >>> {txt.Oopy_function_description[0]}")
            elif back_main == txt.Oopy_help_list[1]:
                print(f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[1]} >>> {txt.Oopy_function_description[1]}")
            elif back_main == txt.Oopy_help_list[2]:
                print(f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[2]} >>> {txt.Oopy_function_description[2]}")
            elif back_main == txt.Oopy_help_list[3]:
                print(f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[3]} >>> {txt.Oopy_function_description[3]}")
            elif back_main == txt.Oopy_help_list[4]:
                print(f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[4]} >>> {txt.Oopy_function_description[4]}")
        elif player_input == txt.Oopy_help_list[4]:
            while True:
                break
        elif player_input == "/exit":
            break



