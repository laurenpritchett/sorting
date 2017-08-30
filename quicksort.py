def quicksort(l):
    if len(l) < 2:
        return l

    mid = len(l / 2)
    pivot = l(mid)

    lo, hi, eq = [], [], []

    for element in l:
        if element < pivot:
            lo.append(element)
        elif element == pivot:
            eq.append(element)
        else:
            hi.append(element)

    return quicksort(lo) + eq + quicksort(hi)
