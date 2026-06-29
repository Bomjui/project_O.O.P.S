import Text as txt
from workbench_g import workbench
import Helpy as hlp
import time

class Game_days_live: #Класс дней, счёт дней, цикл игры самой одним словом
    
    def __init__(self, count_day=0):
        self.count_day = count_day
        self.work = workbench() # Назначение рабочего стола

    def Days_live(self, stdscr):
        self.count_day = 1
        hlp.Left_window_func(stdscr).history_printer(stdscr, txt.History, 3)
        print(f"День {self.count_day}")
        stdscr.clear()
        time.sleep(1)
        
