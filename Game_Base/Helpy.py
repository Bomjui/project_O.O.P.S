from random import choices

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
