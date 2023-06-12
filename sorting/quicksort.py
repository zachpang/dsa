def lomuto_partitioning(arr, lo, hi):
    # select last element as pivot
    pivot = arr[hi]

    # tracks the boundary between left and right partitions
    partitioning_index = lo

    # pass through the arr and look for elements <= pivot, "insert" them into the left partition
    # Note: range(lo, hi) is not inclusive of `hi`.
    # That means the last element/pivot will not be processed in the for loop
    for i in range(lo, hi):
        if arr[i] <= pivot:
            arr[i], arr[partitioning_index] = arr[partitioning_index], arr[i]
            partitioning_index += 1

    # insert the pivot into partitioning_index
    arr[hi], arr[partitioning_index] = arr[partitioning_index], arr[hi]

    return partitioning_index


def quicksort_lomuto(arr, lo, hi):
    if lo >= hi:
        return

    partitioning_index = lomuto_partitioning(arr, lo, hi)

    quicksort_lomuto(arr, lo, partitioning_index - 1)
    quicksort_lomuto(arr, partitioning_index + 1, hi)


def median_of_3(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c


def hoare_partition(arr, lo, hi):
    pivot = median_of_3(arr[lo], arr[(lo + hi) // 2], arr[hi])

    l, r = lo - 1, hi + 1

    while True:
        l += 1
        while arr[l] < pivot:
            l += 1

        r -= 1
        while arr[r] > pivot:
            r -= 1

        if l >= r:
            # l or r can be returned as the partitioning index.
            # we need to be aware of which partition left or right the
            # index belongs to. It will be passed into the next
            # recursion calls as lo/hi args

            # when l and r cross, r is in the left partition
            return r

        arr[l], arr[r] = arr[r], arr[l]


def quicksort_hoare(arr, lo, hi):
    if lo >= hi:
        return

    partitioning_index = hoare_partition(arr, lo, hi)

    quicksort_hoare(arr, lo, partitioning_index)
    quicksort_hoare(arr, partitioning_index + 1, hi)
