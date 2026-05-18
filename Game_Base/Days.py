import Text as txt
from workbench_g import workbench
from Helpy import history_printer
import curses
import time

class Game_days_live: #Класс дней, счёт дней, цикл игры самой одним словом
    
    def __init__(self, count_day):
        self.count_day = count_day
        self.work = workbench() # Назначение рабочего стола

    def Days_live(self):
        curses.wrapper(lambda stdscr: history_printer(stdscr, txt.History, 4))
        print(f"День {self.count_day}")
        time.sleep(0.5)
        self.work.bench() # Запуск рабочего стола
        
Game = Game_days_live(1)
Game.Days_live()