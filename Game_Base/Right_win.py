import asyncio
import curses
from curses.textpad import Textbox, rectangle
import Text as txt
async def time(stdscr, str=0):
    curses.curs_set(0)
    stdscr.nodelay(True)

    #Получаем размеры терминала
    max_y, max_x = stdscr.getmaxyx()
    #Вычисляем размеры для правой половины
    half_width = max_x // 2
    #Синтаксис: curses.newwin(высота, ширина, старт_y, старт_x)
    right_win = curses.newwin(0, 48, 0, 100)
    input_win = curses.newwin(1, 46, 5, 101)
    clock_win = curses.newwin(3, 48, 0, 100)
    #left_win = curses.newwin(max_y, 100, 0, 0)
    async def passage_of_time():
        while txt.timer["hour"] != 6:
            await asyncio.sleep(0.5)
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
        right_win.addstr(3, 1, "Ваше сообшение:")
        right_win.noutrefresh()
        while True:
            clock_win.noutrefresh()
            clock_win.box()
            curses.doupdate()
            clock_win.addstr(1, str+10, txt.days[0])
            clock_win.addstr(1, str+20, "05/08/85")
            clock_win.addstr(2, 1, "-"*46)
            if txt.timer['min'] < 10:
                clock_win.addstr(1, str, f"0{txt.timer['hour']}:0{txt.timer['min']}")
            else:
                clock_win.addstr(1, str, f"0{txt.timer['hour']}:{txt.timer['min']}")
            await asyncio.sleep(0.5)
            if task_timer.done():
                break
            #await asyncio.sleep(0.05)
    async def text_in():
        input_win.nodelay(True)
        box = Textbox(input_win)
        while True:
            ch = input_win.getch()
            if ch != -1:
                if ch in (10, 13):
                    break
                box.do_command(ch)
                input_win.noutrefresh()
            await asyncio.sleep(0.01)
        user_text = box.gather().strip()
        input_win.erase()
        input_win.noutrefresh()
        curses.doupdate()
        return user_text



    await asyncio.gather(game(), text_in())
    #return game_main
    #main_loop = asyncio.run(main())
    #return main_loop, "TIME_OUT"
curses.wrapper(time)
