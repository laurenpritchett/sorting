def bubble_sort(a):
    sorted = False

    while not sorted:
        made_swap = False

        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                made_swap = True

        if not made_swap:
            sorted = True

    return a

test_a = [5, 1, 8, 3, 7]

print test_a
bubble_sort(test_a)
print test_a
