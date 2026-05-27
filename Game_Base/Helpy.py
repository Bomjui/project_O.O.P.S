from random import choices
import sys
import time
from Text import Oopy_help_list
def cursor_off():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def cursor_on():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def delete_symbol():
    sys.stdout.write("\b \b")
    sys.stdout.flush()

def animation_terminal(n, arr, tm, done_showing = False):
    for _ in range(n):
        for frame in arr:
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(tm)
            delete_symbol()
    if done_showing == True:
        print(" [done]")
        time.sleep(tm)
        delete_symbol()

def history_printer(stdscr, txt, string, printer = True, enter_press = True):
    while True:
        if printer == True:
            stdscr.addstr(txt)
        if enter_press == True:
            stdscr.addstr(string, 0, "Нажми Enter чтобы продолжить")
            key = stdscr.getch()
            if key in (10, 13):
                stdscr.clear()
                break
        else:
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

def city_main(stdscr, options, index, string, up=False, up_text=""): # This city plan printer with choice object
    cursor_off()
    count = 0
    while True:
        stdscr.clear()
        if up == True:
            stdscr.addstr(up_text)

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

def OOPY_CHOICE_Function(stdscr, options, index, string, up=False, up_text=""):
    cursor_off()
    count = 0
    a, b, c, d, e = len(options[0]), len(options[1]), len(options[2]), len(options[3]), 7
    button = "next[>]"
    while True:
        stdscr.clear()
        if up == True:
            stdscr.addstr(up_text)

        for i, option in enumerate(options):
            if count == 0 and i == 0:
                stdscr.clear()
                stdscr.addstr(string + i, 0, f"{options[0]} <-- {options[1]}     {options[2]}     {options[3]}     {button}")
            elif count == 1 and i == 0:
                stdscr.clear()
                stdscr.addstr(string + i, 0, f"{options[0]}     {options[1]} <-- {options[2]}     {options[3]}     {button}")
            elif count == 2 and i == 0:
                stdscr.clear()
                stdscr.addstr(string + i, 0, f"{options[0]}     {options[1]}     {options[2]} <-- {options[3]}     {button}")
            elif count == 3 and i == 0:
                stdscr.clear()
                stdscr.addstr(string + i, 0, f"{options[0]}     {options[1]}     {options[2]}     {options[3]} <-- {button}")
            elif count == 4 and i == 0:
                stdscr.clear()
                stdscr.addstr(string + i, 0, f"{options[0]}     {options[1]}     {options[2]}     {options[3]}     {button} <--")

            else:
                stdscr.addstr(string, 0, options[0])
                stdscr.addstr(string, a+5, options[1])
                stdscr.addstr(string, a+b+10, options[2])
                stdscr.addstr(string, a+b+c+15, options[3])
                stdscr.addstr(string, a+b+c+d+20, button)

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
            stdscr.clear()
            stdscr.refresh()
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

