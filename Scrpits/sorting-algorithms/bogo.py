import random as r
import time as t

def check(lst): # Verify if the list is sorted
    max_val = 0
    for value in lst:
        if value > max_val:
            max_val = value
        elif value < max_val:
            return False
    return True

def bogo(lst):
    new_lst = []
    for i in range(len(lst)):
        ch = r.randint(0, len(lst) - 1)
        new_lst.append(lst[ch])
        del lst[ch]
    return new_lst

def bogo_sort(lst):
    shuffled = 0
    while not check(lst):
        lst = bogo(lst)
        shuffled += 1
    return lst, shuffled

if __name__ == "__main__":
    my_list = [r.randint(0, 10) for _ in range(10)] # Defining the list here

    print("Sorting slowly...")

    start_time = t.time()
    result = bogo_sort(my_list)

    print(result[0])
    print("Shuffled", result[1], "times in", t.time() - start_time)
