import asyncio
import curses
import Text as txt
async def time(stdscr, str=0, days = 0):
    curses.curs_set(0)
    stdscr.nodelay(True)

    #Получаем размеры терминала
    max_y, max_x = stdscr.getmaxyx()
    #Вычисляем размеры для правой половины
    half_width = max_x // 2
    #Синтаксис: curses.newwin(высота, ширина, старт_y, старт_x)
    right_win = curses.newwin(0, 48, 0, 100)
    clock_win = curses.newwin(3, 48, 0, 100)
    async def passage_of_time():
        while txt.timer["hour"] != 1:
            await asyncio.sleep(0.05)
            txt.timer["min"] += 1
            if txt.timer["min"] == 60:
                txt.timer["hour"] += 1
                txt.timer["min"] = 0
    async def game():
        task_timer = asyncio.create_task(passage_of_time())
        clock_win.addstr(1, str, f"0{txt.timer['hour']}:0{txt.timer['min']}")
        clock_win.nodelay(True)
        right_win.nodelay(True)
        right_win.box()
        right_win.noutrefresh()
        while True:
            clock_win.noutrefresh()
            clock_win.box()
            curses.doupdate()
            clock_win.addstr(1, str+10, txt.days[days])
            clock_win.addstr(1, str+20, txt.dates[days])
            clock_win.addstr(2, 1, "-"*46)
            if txt.timer['min'] < 10:
                clock_win.addstr(1, str, f"0{txt.timer['hour']}:0{txt.timer['min']}")
            else:
                clock_win.addstr(1, str, f"0{txt.timer['hour']}:{txt.timer['min']}")
            await asyncio.sleep(0.1)



    await asyncio.gather(game())
curses.wrapper(time)
