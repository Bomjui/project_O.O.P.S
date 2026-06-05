from workbench_g import workbench
import curses
import Days
class Game:
    def __init__(self):
        pass

    def analys_game_correct_choice(self):
        pass

    def final_ends(self):
        pass
def main_game_loop(stdscr):
    work = workbench(stdscr)
    work.bench(stdscr)

def days_game_loop(stdscr):
    days = Days.Game_days_live(stdscr)
    days.Days_live(stdscr)

if __name__ == "__main__":
    curses.wrapper(days_game_loop)
    curses.wrapper(main_game_loop)
    curses.curs_set(0)