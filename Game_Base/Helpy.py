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

