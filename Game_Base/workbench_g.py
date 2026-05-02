import time
import Text as txt
import Helpy as hlp
import Email_box as e_box
import os
import curses

class workbench: # Класс рабочего стола тут соеденяются сам игровой стол, ноутбук, типо почты и виртуальный помощьник
    def __init__(self, number = 0, starts_number = 0, save_message = ""):
        self.starts_number = starts_number
        self.save_message = save_message
        self.number = number

    def bench(self): # Цикл рабочего стола
        while True:
            if e_box.message_see(self.number) == False:
                curses.wrapper(lambda stdscr: hlp.main(stdscr, txt.workbench_main, 0, "Your work bench:", 0, 1, True)) # Состояние без сообщения
            else:
                print("[1]Laptop\n[2]Messages-!1!\n[3]") # Состояние с сообщением
            choise_in_bench = int(input("-->")) # Выбор действия
            if choise_in_bench == 1:
                os.system('cls')
                self.laptop()
            if choise_in_bench == 2:
                os.system('cls')
                self.save_message, self.number = e_box.message(self.number, self.save_message)

    def laptop(self):
        while True:
            os.system('cls')
            if self.starts_number == 0:
                print("--O.O.P.S instalation--")
                self.starts_number += 1
            print("[1]Documentation\n [2]Rules\n [3]O.O.P.Y\n  [4]<--EXIT")
            laptop_choise = int(input("-->"))
            if laptop_choise == 1:
                os.system('cls')
                hlp.cursor_off()
                frames = ["|", "/", "--", "\\"]
                print("Opening documentation ", end="")
                hlp.animation_terminal(5, frames, 0.3, True)
                hlp.cursor_on()
                self.documentation()
            elif laptop_choise == 2:
                os.system('cls')
                print("Opening rules")
                time.sleep(1)
                while True:
                    print(txt.rules)
                    exit_rules = int(input())
                    if exit_rules == 4:
                        break
            elif laptop_choise == 3:
                os.system('cls')
                print("")
            else:
                os.system('cls')
                break
        
    def documentation(self):
        print("\n[Documentation] O.O.P.S")
        while True:
            print("Chose file:")
            print(txt.laptop_documentation)
            chose_document = int(input("-->"))
            if chose_document == 5:
                break

    def O_O_P_Y(self):
        pass
        
        