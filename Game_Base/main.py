from workbench_g import workbench
import curses
import Days
import Right_win
import asyncio

class Game:
    def __init__(self):
        pass

    def analys_game_correct_choice(self):
        pass

    def final_ends(self):
        pass
async def days_game_loop(stdscr):
    days = Days.Game_days_live(stdscr)
    days.Days_live(stdscr)
class Game_init:
    def __init__(self):
        self.count = 0
    async def main_game_loop(self, stdscr):
        work = workbench(stdscr)
        await work.bench(stdscr)
        await asyncio.sleep(0.05)
    async def right_win_loop(self, stdscr):
        await Right_win.time(stdscr, 10, self.count)
        await asyncio.sleep(0.05)
    async def main(self, stdscr):
        stdscr.nodelay(True)
        task_0 = asyncio.create_task(days_game_loop(stdscr))
        await task_0
        while self.count <= 4:
            while True:
                task1 = asyncio.create_task(self.main_game_loop(stdscr))
                task2 = asyncio.create_task(self.right_win_loop(stdscr))
                tasks = {task1, task2}
                await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                break
            self.count += 1

def game_loop(stdscr):
    curses.curs_set(0)
    asyncio.run(Game_init().main(stdscr))

if __name__ == "__main__":
    #curses.wrapper(days_game_loop)
    curses.wrapper(game_loop)