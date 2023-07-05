class Solution:
    """
    Algorithm must be better than O(n log n). Should be possible without sorting array.
    In python, you can use a Counter type, and call most_common()

    Solution:
    - Compute counts of each element and store in hashtable/counter. O(N)
    - convert into an array of tuples (element, count). O(N)

    Use quickselect. O(N)
    - choose pivot using median of 3
    - Account for zero-based indexing, so given K = 3, we need to return the right partition when the pivot is sorted into the 3rd last index.
        - i.e. len(nums) = 10, pivot at index = 10 - 3 - 1 = 6.
        - so we need to select the pivot at index 6
        - the right partition would be elements with counts greater than the pivot.

    convert an array of the elements top K elements. O(N)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # compute the frequency of each unique element. O(N)
        element_counts = {}

        for el in nums:
            # since most el should be dupes, we use try-except
            try:
                element_counts[el] += 1
            except KeyError:
                element_counts[el] = 1

        # convert it into an array of tuples (element, count). O(N)
        element_counts_arr = list(element_counts.items())

        # run quickselect on the arr, returning the index for the kth element
        k = len(element_counts_arr) - k - 1
        self.quickselect(element_counts_arr, 0, len(element_counts_arr) - 1, k)

        # take the right partition from kth index
        result = [el for el, count in element_counts_arr[k + 1 :]]

        return result

    def quickselect(self, arr, lo, hi, k):
        if lo >= hi:
            return

        partition_index = self.hoare_partition(arr, lo, hi)

        if k == partition_index:
            return partition_index
        elif k < partition_index:
            return self.quickselect(arr, lo, partition_index, k)
        else:
            return self.quickselect(arr, partition_index + 1, hi, k)

    def hoare_partition(self, arr, lo, hi):
        pivot = self.median_of_3(arr[lo][1], arr[(lo + hi) // 2][1], arr[hi][1])

        l, r = lo - 1, hi + 1

        while True:
            l += 1
            while arr[l][1] < pivot:
                l += 1

            r -= 1
            while arr[r][1] > pivot:
                r -= 1

            # if l crosses or intersects at r
            if l >= r:
                return r

            arr[l], arr[r] = arr[r], arr[l]

    def median_of_3(self, a, b, c):
        if a <= b <= c or c <= b <= a:
            return b
        elif b <= a <= c or c <= a <= b:
            return a
        else:
            return c
