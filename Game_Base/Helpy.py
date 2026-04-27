from random import choices
import sys
import time

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

def random_choiser(arr):
    return choices(arr)
