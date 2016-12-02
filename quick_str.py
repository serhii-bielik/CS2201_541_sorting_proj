
def partition2(DATA, start, end):
    x = DATA[end]
    i = start - 1
    for j in range(start, end):
        if DATA[j].lower() < x.lower():
            i += 1
            DATA[i], DATA[j] = DATA[j], DATA[i]
    DATA[i + 1], DATA[end] = DATA[end], DATA[i + 1]
    return i + 1


def partition(DATA, start, end):
    pivot = DATA[end]
    bottom = start - 1
    top = end

    done = 0
    while not done:

        while not done:
            bottom += 1

            if bottom == top:
                done = 1
                break

            if DATA[bottom].lower() > pivot.lower():
                DATA[top] = DATA[bottom]
                break

        while not done:
            top -= 1

            if top == bottom:
                done = 1
                break

            if DATA[top].lower() < pivot.lower():
                DATA[bottom] = DATA[top]
                break

    DATA[top] = pivot
    return top

def quick_sort(DATA, start, end):
    if start < end:
        split = partition(DATA, start, end)
        quick_sort(DATA, start, split - 1)
        quick_sort(DATA, split + 1, end)