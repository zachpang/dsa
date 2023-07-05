def quickselect(arr, k):
    def partition(arr, low, high):
        pivot_index = median_of_3(arr, low, high)
        pivot = arr[pivot_index]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while arr[i] < pivot:
                i += 1

            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j

            arr[i], arr[j] = arr[j], arr[i]

    def median_of_3(arr, low, high):
        mid = (low + high) // 2

        if arr[low] > arr[mid]:
            if arr[mid] > arr[high]:
                return mid
            elif arr[low] > arr[high]:
                return high
            else:
                return low
        else:
            if arr[low] > arr[high]:
                return low
            elif arr[mid] > arr[high]:
                return high
            else:
                return mid

    def quickselect_recursive(arr, low, high, k):
        print(arr)
        if low == high:
            return arr[low]

        partition_index = partition(arr, low, high)

        if k == partition_index:
            print(arr)
            return arr[k]
        elif k < partition_index:
            return quickselect_recursive(arr, low, partition_index - 1, k)
        else:
            return quickselect_recursive(arr, partition_index + 1, high, k)

    if k <= 0 or k > len(arr):
        return None

    return quickselect_recursive(arr, 0, len(arr) - 1, k - 1)


arr = [2, 1, 2, 1, 2, 1, 1]

print(quickselect(arr, 3))
