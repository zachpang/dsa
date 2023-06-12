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
