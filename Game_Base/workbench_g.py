import time
import Text as txt
import Helpy as hlp
from random import choice
import os
import sys
class workbench: # Класс рабочего стола тут соеденяются сам игровой стол, ноутбук, типо почты и виртуальный помощьник
    def __init__(self, number=0, starts_number = 0, save_message = 0):
        self.number = number
        self.starts_number = starts_number
        self.save_message = save_message

    def bench(self): # Цикл рабочего стола 
        while True:
            print("Your work bench:")
            if self.message_see() == False:
                print("[1]Laptop\n[2]Messages\n[3]") # Состояние без сообщения
            else:
                print("[1]Laptop\n[2]Messages-!1!\n[3]") # Состояние с сообщением
            choise_in_bench = int(input("-->")) # Выбор действия
            if choise_in_bench == 1:
                os.system('cls')
                self.laptop()
            if choise_in_bench == 2:
                os.system('cls')
                self.message()

    def message_see(self):
            if self.number == 1:
                return True
            elif self.number == 0:
                return False
            
    def message(self):
        arr = []
        for i in range(0, 100):
            arr.append(i)
        time.sleep(1)
        print("Your messages:")
        time.sleep(1)

        if self.number == 1:
            print(self.save_message)
        else:
            if choice(arr) <= 250:
                self.save_message = []
                self.number = 1
                self.save_message.append(choice(hlp.for_i_help(txt.messages_str)))
            elif choice(arr) <= 500:
                self.save_message = []
                self.number = 1
                self.save_message.append(choice(hlp.for_i_help(txt.messages_safe)))
            for i in self.save_message:
                self.save_message = i
                print(self.save_message)
        while True:
            os.system('cls')
            messager_exit = int(input("Enter 1 for exit: "))
            if messager_exit == 1:
                break
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
        
        