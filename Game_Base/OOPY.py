import asyncio
import Text as txt
import Helpy as hlp
import curses
from curses.textpad import Textbox


class OPPYS:
    def __init__(self, stdscr, input_win=0, left_win=0, count=2):
        self.input_win = input_win
        self.left_win = left_win
        self.count = count
        # Синтаксис: curses.newwin(высота, ширина, старт_y, старт_x)
        self.input_win = curses.newwin(1, 46, 5, 101)
        self.left_win = hlp.Left_window_func(stdscr).left_window()
        self.animation_win = curses.newwin(1, 40, 2, 0)
        self.left_win.nodelay(True)
        self.input_win.nodelay(True)

    def count_lines(self):
        self.count += 1
        return self.count

    async def terminal_message(self, stdscr, text):
        pass

    async def oppenheimer(self, player_input, save, result):
        try:
            not_symbols = player_input.index("(")
            if player_input[:not_symbols] in txt.Oopy_help_list:
                if player_input[not_symbols] == "(" and player_input[len(player_input) - 1] == ")":
                    save = player_input[not_symbols + 1:len(player_input) - 1]
                    result = player_input[:not_symbols]
                if "(" not in player_input or ")" not in player_input:
                    return "()", True
                return save, result
            else:
                self.left_win.addstr(self.count_lines(), 0, "O.O.P.S[sys]/terminal >>> This is don't function")
                await asyncio.sleep(2)
                self.left_win.refresh()
                return False, False
        except ValueError:
            self.left_win.addstr(self.count_lines(), 0, "O.O.P.S[sys]/terminal >>> This is don't function")
            await asyncio.sleep(2)
            self.left_win.refresh()
            return False, False

    async def text_in(self):
        box = Textbox(self.input_win)
        while True:
            ch = self.input_win.getch()
            if ch != -1:
                if ch in (10, 13):
                    break
                box.do_command(ch)
                self.input_win.noutrefresh()
            await asyncio.sleep(0.01)
        user_text = box.gather().strip()
        self.input_win.erase()
        self.input_win.noutrefresh()
        curses.doupdate()
        return user_text

    async def OOPY_animation(self, stdscr):
        await asyncio.sleep(1)
        await hlp.Left_window_func(stdscr).animation_terminal(2, ("O", "O", "P", "Y"), 0.3,
                                                              "O.O.P.S[sys]/terminal >>> Loading..", True, False,
                                                              0, self.animation_win)

    async def OPPY_main(self, stdscr):
        starting_message = 0
        while True:
            if starting_message == 0:
                self.left_win.addstr(0, 0, f"O.O.P.S[sys]/terminal >>> {txt.Oopy_input_message[0]}")
                self.left_win.refresh()
                await self.text_in()
                starting_message += 1
            while True:
                await self.OOPY_animation(stdscr)
                save, result = "", ""
                player_input = await self.text_in()
                if player_input not in txt.Oopy_help_list:
                    save, result = await self.oppenheimer(player_input, save, result)
                    if result == True:
                        self.left_win.addstr(self.count_lines(), 0,
                                             f"O.O.P.S[sys]/terminal >>> Syntaxis error you forgot paste {save} ")
                        self.left_win.refresh()
                        break
                if player_input in txt.Oopy_help_list:
                    break
                elif result in txt.Oopy_help_list:
                    break
            if player_input == txt.Oopy_help_list[0]:
                await self.OOPY_animation(stdscr)
                self.left_win.addstr(self.count_lines(), 0,
                                     f"O.O.P.S[sys]/terminal >>> Список всех функций: {str(txt.Oopy_help_list)}")
                self.left_win.refresh()
                await asyncio.sleep(1)

            elif result == txt.Oopy_help_list[1]:
                await self.OOPY_animation(stdscr)
                self.left_win.addstr(self.count_lines(), 0, f"O.O.P.S[sys]/terminal >>> {save}")
                self.left_win.refresh()
                await asyncio.sleep(2)
            elif result == txt.Oopy_help_list[2]:
                await self.OOPY_animation(stdscr)
                self.left_win.addstr(self.count_lines(), 0, f"O.O.P.S[sys]/terminal >>> {save}")
                self.left_win.refresh()
                await asyncio.sleep(2)
                # print(f"O.O.P.S[sys]/terminal >>> {save} = ", end="")
                player_input = await self.text_in()
                save_printo, result = await self.oppenheimer(player_input, "", "")
                if f"{result}" == "/printo":
                    self.left_win.addstr(self.count_lines(), 0, f"O.O.P.S[sys]/terminal >>> {save} == {save_printo}")
                    self.left_win.refresh()
                    await asyncio.sleep(2)
                else:
                    self.left_win.addstr(self.count_lines(), 0,
                                         f"O.O.P.S[sys]/terminal >>> Syntaxis error {result} <-- is not /printo")
                    self.left_win.refresh()
                    await asyncio.sleep(2)
            elif player_input == txt.Oopy_help_list[3]:
                await self.OOPY_animation(stdscr)
                back_main = await hlp.Left_window_func(stdscr).OOPY_CHOICE_Function(stdscr, txt.Oopy_help_list, 0, 1,
                                                           True, "O.O.P.S[sys]/terminal >>> Function list <<<")
                if back_main == txt.Oopy_help_list[0]:
                    self.left_win.addstr(self.count_lines(), 0,
                                         f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[0]} >>> {txt.Oopy_function_description[0]}")
                elif back_main == txt.Oopy_help_list[1]:
                    self.left_win.addstr(self.count_lines(), 0,
                                         f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[1]} >>> {txt.Oopy_function_description[1]}")
                elif back_main == txt.Oopy_help_list[2]:
                    self.left_win.addstr(self.count_lines(), 0,
                                         f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[2]} >>> {txt.Oopy_function_description[2]}")
                elif back_main == txt.Oopy_help_list[3]:
                    self.left_win.addstr(self.count_lines(), 0,
                                         f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[3]} >>> {txt.Oopy_function_description[3]}")
                elif back_main == txt.Oopy_help_list[4]:
                    self.left_win.addstr(self.count_lines(), 0,
                                         f"O.O.P.S[sys]/terminal >>> {txt.Oopy_help_list[4]} >>> {txt.Oopy_function_description[4]}")
                self.left_win.refresh()
                await asyncio.sleep(2)
            elif player_input == txt.Oopy_help_list[4]:
                while True:
                    break
            elif player_input == "/exit":
                break
