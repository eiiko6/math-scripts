import random

items = ["Item A", "Item B", "Item C", "Item D", "Item E"]
random.shuffle(items)

def splitlist(array):
    if len(array) % 2 == 0:
        n = int(len(array) / 2)
    else:
        n = int(len(array) / 2 + 1)

    first_half = array[:n]
    sec_half = array[n:]

    return [first_half, sec_half]

while len(items) > 1:
    split = splitlist(items)
    print("Split: " + str(split))

    items = split[random.randint(0, 1)]

print("Chosen item: " + str(items[0]))
