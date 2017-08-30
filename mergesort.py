def merge_sort(l):
    if len(l) < 2:
        return l

    mid = int(len(l) / 2)
    l1 = merge_sort(l[:mid])
    l2 = merge_sort(l[mid:])

    return merge_sorted_arrays(l1, l2)


def merge_sorted_arrays(a1, a2):
    new_array = []

    while a1 or a2:
        if not a1:
            new_array.append(a2.pop(0))
        elif not a2:
            new_array.append(a1.pop(0))
        elif a1[0] < a2[0]:
            new_array.append(a1.pop(0))
        else:
            new_array.append(a2.pop(0))

    return new_array

print merge_sort([5, 3, 2, 8, 6, 7, 1])
