def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                made_swap = True

        if not made_swap:
            break

    return a

test_a = [5, 1, 8, 3, 7]

print test_a
bubble_sort(test_a)
print test_a
