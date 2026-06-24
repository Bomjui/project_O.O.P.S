import asyncio
import time
import Text as txt
import Helpy as hlp
import City_place_sectors_happen as cpsh
import OOPY
import os
import curses
from Creatures import paths, Creatures_choice
async def test(stdscr):
    main_bench_choice = hlp.main(stdscr, txt.workbench_main, 0, "Your work bench:", 0, 1, True, False, 0)
    await main_bench_choice
class workbench: # Класс рабочего стола тут соеденяются сам игровой стол, ноутбук, типо почты и виртуальный помощьник
    def __init__(self, number_message = 0, number_sectors = 0, save_message_sectors = "", starts_number = 0, save_message = "", frames=""):
        self.starts_number = starts_number
        self.save_message = save_message
        self.number_message = number_message
        self.save_message_sectors = save_message_sectors
        self.number_sectors = number_sectors
        self.frames = frames

    def left_window(self, stdscr):
        max_y, max_x = stdscr.getmaxyx()
        half_width = 100
        left_win = curses.newwin(max_y, half_width, 0, 0)
        return left_win
    async def bench(self, stdscr): # Цикл рабочего стола
        curses.curs_set(0)
        while True:
            if cpsh.message_see(self.number_message) == False:
                main_bench_choice = await hlp.main(stdscr, txt.workbench_main, 0, "Your work bench:", 0, 1, True, False, 0) # Состояние без сообщения
            else:
                main_bench_choice = await hlp.main(stdscr, txt.workbench_main_with_message, 0, "Your work bench:", 0, 1, True, False, 0)# Состояние с сообщением
            if main_bench_choice == txt.workbench_main[0]:
                self.left_window(stdscr).clear()
                await self.laptop(stdscr)
            elif main_bench_choice == txt.workbench_main[1] or main_bench_choice == txt.workbench_main_with_message[1]:
                self.save_message, self.number_message = None, None
            await asyncio.sleep(0.05)

    async def laptop(self, stdscr):
        curses.curs_set(0)
        while True:
            self.frames = ["|", "/", "--", "\\"]
            if self.starts_number == 0:
                hlp.cursor_off()
                await hlp.animation_terminal(stdscr, 2, self.frames, 0.1, "--O.O.P.S instalation--", True)
                hlp.cursor_on()
                self.starts_number += 1
            laptop_main_choice = await hlp.main(stdscr, txt.laptop_main, 0, "Your work bench:", 0, 1, True)
            if laptop_main_choice == txt.laptop_main[0]:
                self.left_window(stdscr).clear()
                await self.documentation(stdscr)
            elif laptop_main_choice == txt.laptop_main[1]:
                self.left_window(stdscr).clear()
                await self.rules(stdscr)
            elif laptop_main_choice == txt.laptop_main[2]:
                city_main_map = await self.cities_map(stdscr)
                wait, count = 0, 0
                while city_main_map != "[X]EXIT":
                    if 1 in txt.city_place_message_save[city_main_map]:
                        self.number_sectors = 1
                        self.save_message_sectors = txt.city_place_message_save[city_main_map][1]
                    else:
                        self.number_sectors = 0
                    if count > 0:
                        self.save_message_sectors, self.number_sectors, action = await cpsh.message(stdscr, self.number_sectors,
                                                                                              self.save_message_sectors,
                                                                                              city_main_map, wait)
                        count = 0
                    else:
                        self.save_message_sectors, self.number_sectors, action = await cpsh.message(stdscr, self.number_sectors,
                                                                                              self.save_message_sectors,
                                                                                              city_main_map)
                    txt.city_place_message_save[city_main_map] = [1, self.save_message_sectors]
                    if action == True:
                        break
                    elif action == False:
                        self.left_window(stdscr).clear()
                        city_main_map = await self.cities_map(stdscr)
                    else:
                        Creature_name = await Creatures_choice(stdscr)
                        self.left_window(stdscr).clear()
                        city_distance = await hlp.city_distances(stdscr, txt.city_places, 0, 1,
                                                                await paths(city_main_map),
                                                                txt.creatures_names[Creature_name][1],
                                                                True,
                                                                "---[City plan]------------------------------------------------------------------------------")
                        if city_distance > 0:
                            wait = city_distance
                            txt.city_place_message_save[city_main_map] = []
                            count += 1
            elif laptop_main_choice == txt.laptop_main[3]:
                self.left_window(stdscr).clear()
                await self.O_O_P_Y(stdscr)
            elif laptop_main_choice == txt.laptop_main[4]:
                while True:
                    print("News")
                    break
            else:
                os.system('cls')
                break

    async def rules(self, stdscr):
        curses.curs_set(0)
        await hlp.animation_terminal(stdscr, 2, self.frames, 0.1, "Opening rules", True)
        hlp.cursor_on()
        time.sleep(1)
        rules_s = await hlp.main(stdscr, txt.rules, 0,
        "Внимание если ты это читаешь это значит что ты отвественнен.Правила что ты никогда не должен нарушать:",
        0, 1,True)
        self.left_window(stdscr).clear()
        
    async def documentation(self, stdscr):
        curses.curs_set(0)
        await hlp.animation_terminal(stdscr, 5, self.frames, 0.3,  "Opening documentation ",  True)
        hlp.cursor_on()
        while True:
            documentation_main_choice = await hlp.main(stdscr, txt.laptop_documentation, 0,
                                                                               "[Documentation] O.O.P.S\t|Chose file:|", 0, 1, True)
            if documentation_main_choice == txt.laptop_documentation[4]:
                self.left_window(stdscr).clear()
                break

    async def cities_map(self, stdscr):
        curses.curs_set(0)
        while True:
            city_main_map = await hlp.city_main(stdscr, txt.city_places, 0, 1,
            True, "---[City plan]------------------------------------------------------------------------------")
            self.left_window(stdscr).clear()
            return city_main_map
    async def O_O_P_Y(self, stdscr):
        self.left_window(stdscr).clear()
        oopy_main = await OOPY.OPPY_main(stdscr)
        
        