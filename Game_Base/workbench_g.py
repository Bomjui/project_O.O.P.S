import time
import Text as txt
import Helpy as hlp
import City_place_sectors_happen as cpsh
import OOPY
import os
import curses


class workbench: # Класс рабочего стола тут соеденяются сам игровой стол, ноутбук, типо почты и виртуальный помощьник
    def __init__(self, number_message = 0, number_sectors = 0, save_message_sectors = "", starts_number = 0, save_message = "", frames=""):
        self.starts_number = starts_number
        self.save_message = save_message
        self.number_message = number_message
        self.save_message_sectors = save_message_sectors
        self.number_sectors = number_sectors
        self.frames = frames
    def bench(self): # Цикл рабочего стола
        while True:
            if cpsh.message_see(self.number_message) == False:
                main_bench_choice = curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.workbench_main, 0, "Your work bench:", 0, 1, True)) # Состояние без сообщения
            else:
                main_bench_choice = curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.workbench_main_with_message, 0, "Your work bench:", 0, 1, True))# Состояние с сообщением
            if main_bench_choice == txt.workbench_main[0]:
                os.system('cls')
                self.laptop()
            elif main_bench_choice == txt.workbench_main[1] or main_bench_choice == txt.workbench_main_with_message[1]:
                self.save_message, self.number_message = None, None

    def laptop(self):
        while True:
            os.system('cls')
            self.frames = ["|", "/", "--", "\\"]
            if self.starts_number == 0:
                hlp.cursor_off()
                print("--O.O.P.S instalation--", end="")
                hlp.animation_terminal(2, self.frames, 0.1, True)
                hlp.cursor_on()
                self.starts_number += 1
            laptop_main_choice = curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.laptop_main, 0, "Your work bench:", 0, 1, True))
            if laptop_main_choice == txt.laptop_main[0]:
                os.system('cls')
                self.documentation()
            elif laptop_main_choice == txt.laptop_main[1]:
                os.system('cls')
                self.rules()
            elif laptop_main_choice == txt.laptop_main[2]:
                city_main_map = self.cities_map()
                while city_main_map != txt.city_places[24]:
                    os.system('cls')
                    if 1 in txt.city_place_message_save[city_main_map]:
                        self.number_sectors = 1
                        self.save_message_sectors = txt.city_place_message_save[city_main_map][1]
                    else:
                        self.number_sectors = 0
                    self.save_message_sectors, self.number_sectors, action = cpsh.message(self.number_sectors, self.save_message_sectors, city_main_map)

                    txt.city_place_message_save[city_main_map] = [1, self.save_message_sectors]

                    if action == True:
                        break
            elif laptop_main_choice == txt.laptop_main[3]:
                self.O_O_P_Y()
            elif laptop_main_choice == txt.laptop_main[4]:
                while True:
                    print("News")
                    time.sleep(2)
                    break
            else:
                os.system('cls')
                break

    def rules(self):
        hlp.cursor_off()
        print("Opening rules", end="")
        hlp.animation_terminal(2, self.frames, 0.1, True)
        hlp.cursor_on()
        time.sleep(1)
        curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.rules, 0,
        "Внимание если ты это читаешь это значит что ты отвественнен.Правила что ты никогда не должен нарушать:",
        0, 1,True))
        
    def documentation(self):
        hlp.cursor_off()
        print("Opening documentation ", end="")
        hlp.animation_terminal(5, self.frames, 0.3, True)
        hlp.cursor_on()
        while True:
            documentation_main_choice = curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.laptop_documentation, 0,
                                                                               "[Documentation] O.O.P.S\t|Chose file:|", 0, 1, True))
            if documentation_main_choice == txt.laptop_documentation[4]:
                os.system('cls')
                break

    def cities_map(self):
        while True:
            city_main_map = curses.wrapper(lambda stdscr: hlp.city_main(stdscr, txt.city_places, 0, 1,
                                                                        True, "---[City plan]------------------------------------------------------------------------------"))
            return city_main_map
    def O_O_P_Y(self):
        oopy_main = OOPY.OPPY_main()
        
        