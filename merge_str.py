
def merge_sort(A):
    size = len(A)
    if size != 1:
        center = size / 2
        LEFT = []
        for i in range(0, center):
            LEFT.append(A[i])
        RIGHT = []
        for i in range(center, size):
            RIGHT.append(A[i])

        LEFT = merge_sort(LEFT)
        RIGHT = merge_sort(RIGHT)

        return merge(LEFT, RIGHT)
    return A

def merge(LEFT, RIGHT):
    SORTED = []
    leftI = 0
    rightI = 0

    while (leftI < len(LEFT)) and (rightI < len(RIGHT)):
        if LEFT[leftI].lower() < RIGHT[rightI].lower():
            SORTED.append(LEFT[leftI])
            leftI += 1
        else:
            SORTED.append(RIGHT[rightI])
            rightI += 1

    REST = []
    restI = 0
    if leftI >= len(LEFT):
        REST = RIGHT
        restI = rightI
    else:
        REST = LEFT
        restI = leftI

    for i in range(restI, len(REST)):
        SORTED.append(REST[i])
    return SORTED
