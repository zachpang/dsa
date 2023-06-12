from quicksort import quicksort_lomuto, quicksort_hoare


def test_quicksort_lomuto():
    arr = []
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == []

    arr = [5]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [5]

    arr = [3, 7, 2, 5, 2, 9, 7]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [2, 2, 3, 5, 7, 7, 9]

    arr = [1, 2, 3, 4, 5]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [-2, 4, -7, 0, -1]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [-7, -2, -1, 0, 4]

    arr = [1000000, 999999, 100000, 99999]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [99999, 100000, 999999, 1000000]

    arr = [9, 1, 5, 3, 7, 2]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 5, 7, 9]

    arr = [8, 8, 8, 8, 8]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [8, 8, 8, 8, 8]

    arr = [2, 1, 2, 1, 2, 1, 1]
    quicksort_lomuto(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 1, 1, 2, 2, 2]


test_quicksort_lomuto()


def test_quicksort_hoare():
    arr = []
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == []

    arr = [5]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [5]

    arr = [3, 7, 2, 5, 2, 9, 7]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [2, 2, 3, 5, 7, 7, 9]

    arr = [1, 2, 3, 4, 5]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [-2, 4, -7, 0, -1]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [-7, -2, -1, 0, 4]

    arr = [1000000, 999999, 100000, 99999]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [99999, 100000, 999999, 1000000]

    arr = [9, 1, 5, 3, 7, 2]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 5, 7, 9]

    arr = [8, 8, 8, 8, 8]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [8, 8, 8, 8, 8]

    arr = [2, 1, 2, 1, 2, 1, 1]
    quicksort_hoare(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 1, 1, 2, 2, 2]


test_quicksort_hoare()
