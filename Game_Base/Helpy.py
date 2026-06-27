import curses
from random import choices
import sys
from Text import Oopy_help_list
import heapq
import asyncio

async def dijkstara_with_path(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    predecessors = {}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances.get(current_vertex, float("infinity")):
            continue
        for neighbor, weight in graph.get(current_vertex, {}).items():
            distance = current_distance + weight
            if distance < distances.get(neighbor, float("infinity")):
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
        await asyncio.sleep(0.05)
    return distances, predecessors

async def get_exact_path(predecessors, start, target):
    if target not in predecessors and target != start:
        return []
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    path.reverse()
    await asyncio.sleep(0.05)
    return path

def cursor_off():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def cursor_on():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def delete_symbol():
    sys.stdout.write("\b \b")
    sys.stdout.flush()

class Left_window_func:
    def __init__(self, stdscr, left_win=0):
        max_y, max_x = stdscr.getmaxyx()
        half_width = 100
        self.left_win = left_win
        self.left_win = curses.newwin(max_y, half_width, 0, 0)

    def left_window(self):
        return self.left_win

    async def animation_terminal(self, n, arr, tm, word, done_showing = False, delete = True, string = 0, win = None):
        if win == None:
            win = self.left_win
            self.left_win.nodelay(True)
        for _ in range(n):
            for frame in arr:
                if delete == True:
                    win.erase()
                win.addstr(string, 0, word)
                win.addstr(string, len(word), frame)
                win.refresh()
                await asyncio.sleep(tm)
        if done_showing == True:
            win.addstr(string, 0, " [done]")
            await asyncio.sleep(tm)
            if delete == True:
                win.erase()

    def history_printer(self, stdscr, txt, string, printer = True, enter_press = True):
        while True:
            if printer == True:
                self.left_win.addstr(txt)
            if enter_press == True:
                self.left_win.addstr(string, 0, "Нажми Enter чтобы продолжить")
                self.left_win.refresh()
                key = stdscr.getch()
                if key in (10, 13):
                    self.left_win.clear()
                    break
            else:
                self.left_win.erase()
                break

    async def main(self, stdscr, options, index, up_text="", down_text="", string=0, up=False, down=False, count=0, two=False, two_text=""):
        cursor_off()
        stdscr.nodelay(True)
        game_state = {"time_left": count}
        async def timer():
            while game_state["time_left"] > 0:
                await asyncio.sleep(1)
                game_state["time_left"] -= 1
        async def game(index):
            asyncio.create_task(timer())
            while True:
                key = stdscr.getch()

                if key in (ord("w"), ord("W")):
                    index = (index - 1) % len(options)

                elif key in (ord("s"), ord("S")):
                    index = (index + 1) % len(options)

                elif key in (10, 13):
                    self.left_win.erase()
                    self.left_win.noutrefresh()
                    return options[index]
                self.left_win.erase()

                if up == True:
                    self.left_win.addstr(up_text)
                if two == True and game_state["time_left"] == 0:
                    self.left_win.addstr(1, 0, two_text)
                elif game_state["time_left"] > 0:
                    self.left_win.move(1, 0)
                    self.left_win.clrtoeol()
                    self.left_win.addstr(1, 10, f"Wait: {game_state['time_left']}")
                for i, option in enumerate(options):
                    if i == index:
                        self.left_win.addstr(string + i, 0, f"{option} <--")
                    else:
                        self.left_win.addstr(string + i, 0, option)
                if down == True:
                    self.left_win.addstr(down_text)

                self.left_win.noutrefresh()
                curses.doupdate()
                await asyncio.sleep(0.05)

        #async def mains():
        game_main = await game(index)
        return game_main
        #main_loop = asyncio.run(main())
        #return main_loop

    async def city_main(self, stdscr, options, index, string, up=False, up_text=""): # This city plan printer with choice object
        count = 0
        while True:
            self.left_win.erase()
            if up == True:
                self.left_win.addstr(up_text)

            gen = city_tkinter(options, 5) #
            a = await anext(gen)
            b = await anext(gen)
            c = await anext(gen)
            d = await anext(gen)
            e = await anext(gen)


            for i, option in enumerate(a):
                if count == 0 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} <-- \t    {b[i]} \t        {c[i]} \t    {d[i]} \t\t{e[i]}")
                elif count == 1 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} \t    {b[i]} <--       {c[i]} \t    {d[i]} \t\t{e[i]}")
                elif count == 2 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} <-- \t    {d[i]} \t\t{e[i]}")
                elif count == 3 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} \t    {d[i]} <-- \t{e[i]}")
                elif count == 4 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} \t    {d[i]} \t\t{e[i]} <--")

                else:
                    self.left_win.addstr(string + i, 80, e[i])
                    self.left_win.addstr(string + i, 60, d[i])
                    self.left_win.addstr(string + i, 40, c[i])
                    self.left_win.addstr(string + i, 20, b[i])
                    self.left_win.addstr(string + i, 0, option)

            key = stdscr.getch()

            if key in (ord("w"), ord("W")):
                if index == 0:
                    index = 0
                else:
                    index -= 1


            elif key in (ord("s"), ord("S")):
                if index >= 4:
                    index = 4
                else:
                    index += 1

            elif key in (ord("d"), ord("D")):
                if count >= 4:
                    count = 4
                else:
                    count += 1

            elif key in (ord("a"), ord("A")):
                if count == 0:
                    count = 0
                else:
                    count -= 1

            elif key in (10, 13):
                self.left_win.erase()
                self.left_win.noutrefresh()
                if count == 0:
                    return a[index]
                elif count == 1:
                    return b[index]
                elif count == 2:
                    return c[index]
                elif count == 3:
                    return d[index]
                elif count == 4:
                    return e[index]
            self.left_win.noutrefresh()
            curses.doupdate()

    async def OOPY_CHOICE_Function(self, stdscr, options, index, string, up=False, up_text=""):
        cursor_off()
        count = 0
        a, b, c, d, e = len(options[0]), len(options[1]), len(options[2]), len(options[3]), 7
        button = "next[>]"
        while True:
            self.left_win.erase()
            if up == True:
                self.left_win.addstr(up_text)

            for i, option in enumerate(options):
                if count == 0 and i == 0:
                    self.left_win.erase()
                    self.left_win.addstr(string + i, 0, f"{options[0]} <-- {options[1]}     {options[2]}     {options[3]}     {button}")
                elif count == 1 and i == 0:
                    self.left_win.erase()
                    self.left_win.addstr(string + i, 0, f"{options[0]}     {options[1]} <-- {options[2]}     {options[3]}     {button}")
                elif count == 2 and i == 0:
                    self.left_win.erase()
                    self.left_win.addstr(string + i, 0, f"{options[0]}     {options[1]}     {options[2]} <-- {options[3]}     {button}")
                elif count == 3 and i == 0:
                    self.left_win.erase()
                    self.left_win.addstr(string + i, 0, f"{options[0]}     {options[1]}     {options[2]}     {options[3]} <-- {button}")
                elif count == 4 and i == 0:
                    self.left_win.erase()
                    self.left_win.addstr(string + i, 0, f"{options[0]}     {options[1]}     {options[2]}     {options[3]}     {button} <--")

                else:
                    self.left_win.addstr(string, 0, options[0])
                    self.left_win.addstr(string, a+5, options[1])
                    self.left_win.addstr(string, a+b+10, options[2])
                    self.left_win.addstr(string, a+b+c+15, options[3])
                    self.left_win.addstr(string, a+b+c+d+20, button)

            key = stdscr.getch()

            if key in (ord("d"), ord("D")):
                if count >= 4:
                    count = 4
                else:
                    count += 1

            elif key in (ord("a"), ord("A")):
                if count == 0:
                    count = 0
                else:
                    count -= 1

            elif key in (10, 13):
                self.left_win.erase()
                self.left_win.noutrefresh()
                cursor_on()
                if options[count] != "Soon":
                    if count == 0:
                        return options[0]
                    elif count == 1:
                        return options[1]
                    elif count == 2:
                        return options[2]
                    elif count == 3:
                        return options[3]
                if count == 4:
                    if button == "next[>]":
                        options = options[4:]
                        for _ in range(5-len(options)):
                            options.append("Soon")
                        button = "[<]back"
                    elif button == "[<]back":
                        options = Oopy_help_list
                        button = "next[>]"
                    a, b, c, d, e = len(options[0]), len(options[1]), len(options[2]), len(options[3]), 7
                    count = 0
            self.left_win.noutrefresh()
            curses.doupdate()

    async def city_distances(self, stdscr, options, index, string, distance, speed, up=False, up_text=""): # This city plan printer with choice object
        cursor_off()
        stdscr.nodelay(True)
        nums = await city_numbers(options, distance)
        gens = city_tkinter(nums, 2)
        iteration = 0
        while True:
            try:
                index, count = await anext(gens)
                iteration += 1
            except StopAsyncIteration:
                return 0
            self.left_win.erase()
            if up == True:
                self.left_win.addstr(up_text)

            gen = city_tkinter(options, 5) #
            a = await anext(gen)
            b = await anext(gen)
            c = await anext(gen)
            d = await anext(gen)
            e = await anext(gen)


            for i, option in enumerate(a):
                if count == 0 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} <-- \t    {b[i]} \t        {c[i]} \t    {d[i]} \t\t{e[i]}")
                elif count == 1 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} \t    {b[i]} <--       {c[i]} \t    {d[i]} \t\t{e[i]}")
                elif count == 2 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} <-- \t    {d[i]} \t\t{e[i]}")
                elif count == 3 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} \t    {d[i]} <-- \t{e[i]}")
                elif count == 4 and i == index:
                    self.left_win.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} \t    {d[i]} \t\t{e[i]} <--")

                else:
                    self.left_win.addstr(string + i, 80, e[i])
                    self.left_win.addstr(string + i, 60, d[i])
                    self.left_win.addstr(string + i, 40, c[i])
                    self.left_win.addstr(string + i, 20, b[i])
                    self.left_win.addstr(string + i, 0, option)
            await asyncio.sleep(0.05)
            self.left_win.noutrefresh()
            key = stdscr.getch()
            if key in (10, 13):
                self.left_win.erase()
                self.left_win.noutrefresh()
                cursor_on()
                return len(distance)-iteration
            await asyncio.sleep(speed)
            curses.doupdate()
def for_i_help(arr):
    a = []
    for i in arr.values():
        a.append(i)
    return a

def for_printer(arr, numbers_paste = False):
    count = 0
    if numbers_paste == False:
        for i in arr:
            print(i)
    else:
        for i in arr:
            count += 1
            print(f"{count}: {i}")

def random_choicer(arr):
    return choices(arr)

def city_map_printer(arr, n):
    count = 0
    for i in arr:
        if count == n:
            count = 1
            print(f"\n{i}", end="  ")
        else:
            count += 1
            print(i, end="  ")

async def city_tkinter(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]

async def city_numbers(options, distance):
    gen = city_tkinter(options, 5)
    save = []
    a = await anext(gen)
    b = await anext(gen)
    c = await anext(gen)
    d = await anext(gen)
    e = await anext(gen)
    for i in distance:
        if i in a:
            num = a.index(i)
            save += num, 0
        elif i in b:
            num = b.index(i)
            save += num, 1
        elif i in c:
            num = c.index(i)
            save += num, 2
        elif i in d:
            num = d.index(i)
            save += num, 3
        elif i in e:
            num = e.index(i)
            save += num, 4
    return save