from random import choices
import sys
import time
import curses

def cursor_off():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def cursor_on():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def delete_symbol(n = 1):
    sys.stdout.write("\b \b" * n)
    sys.stdout.flush()

def animation_terminal(n, arr, tm, done_showing = False):
    for _ in range(n):
        for frame in arr:
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(tm)
            delete_symbol()
    if done_showing == True:
        print(" done")
        time.sleep(tm)
        delete_symbol(2)

def history_printer(stdscr, txt, string):
    while True:
        stdscr.addstr(txt)
        stdscr.addstr(string, 0, "Нажми Enter чтобы продолжить")
        key = stdscr.getch()
        if key in (10, 13):
            stdscr.clear()
            break


def main(stdscr, options, index, up_text="", down_text="", string=0, up=False, down=False):
    cursor_off()
    stdscr.clear()
    while True:
        stdscr.clear()
        if up == True:
            stdscr.addstr(up_text)

        for i, option in enumerate(options):
            if i == index:
                stdscr.addstr(string + i, 0, f"{option} <--")
            else:
                stdscr.addstr(string + i, 0, option)

        if down == True:
            stdscr.addstr(down_text)

        key = stdscr.getch()

        if key in (ord("w"), ord("W")):
            index = (index - 1) % len(options)

        elif key in (ord("s"), ord("S")):
            index = (index + 1) % len(options)

        elif key in (10, 13):
            stdscr.clear()
            stdscr.refresh()
            cursor_on()
            return options[index]

def city_main(stdscr, options, index, indey, string): # This city plan printer with choice object
    cursor_off()
    count = 0
    while True:
        stdscr.clear()


        gen = city_tkinter(options, 5) #
        a = next(gen)
        b = next(gen)
        c = next(gen)
        d = next(gen)
        e = next(gen)


        for i, option in enumerate(a):
            if count == 0 and i == index:
                stdscr.addstr(string + i, 0, f"{option} <-- \t    {b[i]} \t        {c[i]} \t    {d[i]} \t\t{e[i]}")
            elif count == 1 and i == index:
                stdscr.addstr(string + i, 0, f"{option} \t    {b[i]} <--       {c[i]} \t    {d[i]} \t\t{e[i]}")
            elif count == 2 and i == index:
                stdscr.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} <-- \t    {d[i]} \t\t{e[i]}")
            elif count == 3 and i == index:
                stdscr.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} \t    {d[i]} <-- \t{e[i]}")
            elif count == 4 and i == index:
                stdscr.addstr(string + i, 0, f"{option} \t    {b[i]} \t        {c[i]} \t    {d[i]} \t\t{e[i]} <--")

            else:
                stdscr.addstr(string + i, 80, e[i])
                stdscr.addstr(string + i, 60, d[i])
                stdscr.addstr(string + i, 40, c[i])
                stdscr.addstr(string + i, 20, b[i])
                stdscr.addstr(string + i, 0, option)

        key = stdscr.getch()

        if key in (ord("w"), ord("W")):
            index = (index - 1) % len(options)

        elif key in (ord("s"), ord("S")):
            index = (index + 1) % len(options)

        elif key in (ord("d"), ord("D")):
            indey = (indey + 1) % len(options)
            if count >= 4:
                count = 4
            else:
                count += 1

        elif key in (ord("a"), ord("A")):
            indey = (indey - 1) % len(options)
            if count == 0:
                count = 0
            else:
                count -= 1

        elif key in (10, 13):
            stdscr.clear()
            stdscr.refresh()
            cursor_on()
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

def city_tkinter(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]

