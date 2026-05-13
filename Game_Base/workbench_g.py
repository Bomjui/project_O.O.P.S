import time
import Text as txt
import Helpy as hlp
import Email_box as e_box
import os
import curses

class workbench: # Класс рабочего стола тут соеденяются сам игровой стол, ноутбук, типо почты и виртуальный помощьник
    def __init__(self, number = 0, starts_number = 0, save_message = "", frames=""):
        self.starts_number = starts_number
        self.save_message = save_message
        self.number = number
        self.frames = frames
    def bench(self): # Цикл рабочего стола
        while True:
            if e_box.message_see(self.number) == False:
                main_bench_choice = curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.workbench_main, 0, "Your work bench:", 0, 1, True)) # Состояние без сообщения
            else:
                main_bench_choice = curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.workbench_main_with_message, 0, "Your work bench:", 0, 1, True))# Состояние с сообщением
            if main_bench_choice == txt.workbench_main[0]:
                os.system('cls')
                self.laptop()
            elif main_bench_choice == txt.workbench_main[1] or main_bench_choice == txt.workbench_main_with_message[1]:
                os.system('cls')
                self.save_message, self.number = e_box.message(self.number, self.save_message)

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
                a = self.cities_map()
                while True:
                    print(f"Your choice {a}")
                    a = int(input())
                    if a == 0:
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
            documentation_main_choice = curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.laptop_documentation, 0, "[Documentation] O.O.P.S\t|Chose file:|", 0, 1, True))
            if documentation_main_choice == txt.laptop_documentation[4]:
                os.system('cls')
                break

    def cities_map(self):
        while True:
            a = curses.wrapper(lambda stdscr: hlp.city_main(stdscr, txt.city_places, 0, 0, 0))
            return a
    def O_O_P_Y(self):
        pass
        
        