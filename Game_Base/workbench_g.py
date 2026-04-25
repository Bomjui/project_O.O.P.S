import time
import Text as txt
import Helpy as hlp
from random import choice
class workbench: # Класс рабочего стола тут соеденяются сам игровой стол, ноутбук, типо почты и виртуальный помощьник
    def __init__(self, number=0, starts_number = 0):
        self.number = number
        self.starts_number = starts_number

    def bench(self): # Цикл рабочего стола 
        while True:
            print("Your work bench:")
            if self.message_see() == False:
                print("[1]Laptop\n[2]Messages\n[3]") # Состояние без сообщения
            else:
                print("[1]Laptop\n[2]Messages-!1!\n[3]") # Состояние с сообщением
            choise_in_bench = int(input("-->")) # Выбор действия
            if choise_in_bench == 1:
                self.laptop()
            if choise_in_bench == 2:
                self.message()

    def message_see(self):
            message = self.number
            if message == 1:
                return True
            elif self.number == 0:
                return False
            
    def message(self):
        arr = []
        for i in range(0, 100):
            arr.append(i)
        print("Your messages:")

        def message_count():
            while True:
                if choice(arr) <= 500:
                    self.number = 1
                    return choice(txt.messages_safe.values())
                elif choice(arr) <= 250: 
                    return choice(txt.messages_str.values())
                    
        print(message_count())
        
    def laptop(self):
        while True:
            if self.starts_number == 0:
                print("--O.O.P.S instalation--")
                self.starts_number += 1
            print("[1]Documentation\n [2]Rules\n [3]O.O.P.Y\n  [4]<--EXIT")
            laptop_choise = int(input("-->"))
            if laptop_choise == 1:
                print("Opening documentation")
                time.sleep(1)
                self.documentation()
            elif laptop_choise == 2:
                print("Opening rules")
                time.sleep(1)
                while True:
                    print(txt.rules)
                    exit_rules = int(input())
                    if exit_rules == 4:
                        break
            elif laptop_choise == 3:
                print("")
            else:
                break
        
    def documentation(self):
        print("[Documentation] O.O.P.S")
        while True:
            print("Chose file:")
            print(txt.laptop_documentation)
            chose_document = int(input("-->"))
            if chose_document == 5:
                break

    def O_O_P_Y(self):
        pass
        
        