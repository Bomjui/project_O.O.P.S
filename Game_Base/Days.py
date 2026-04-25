import Text as txt
from workbench_g import workbench

class Game_days_live: #Класс дней, счёт дней, цикл игры самой одним словом
    
    def __init__(self, count_day):
        self.count_day = count_day
        self.work = workbench()

    def Days_live(self):
        print(txt.History[1])
        print(f"День - {self.count_day}") #Счёт прожитых дней
        self.work.bench() # Запуск рабочего стола
        
Game = Game_days_live(1)
Game.Days_live()