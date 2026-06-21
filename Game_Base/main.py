from workbench_g import workbench, test
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
async def main_game_loop(stdscr):
    while True:
        work = workbench(stdscr)
        task = await work.bench(stdscr)
        await asyncio.sleep(0.05)

async def game(stdscr):
    while True:
        games = test(stdscr)
        await games
def days_game_loop(stdscr):
    days = Days.Game_days_live(stdscr)
    days.Days_live(stdscr)
async def right_win_loop(stdscr):
    while True:
        await Right_win.time(stdscr, 10)
        await asyncio.sleep(0.1)
async def main(stdscr):
    stdscr.nodelay(True)

    await asyncio.gather(
        #game(stdscr)
        main_game_loop(stdscr),
        right_win_loop(stdscr)
    )
def game_loop(stdscr):
    asyncio.run(main(stdscr))

if __name__ == "__main__":
    curses.wrapper(days_game_loop)
    curses.wrapper(game_loop)
    curses.curs_set(0)