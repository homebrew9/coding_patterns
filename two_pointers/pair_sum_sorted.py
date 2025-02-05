from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    def bsearch(arr, t):
        print(f'\tarr, t = {arr}, {t}')
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == t:
                return mid
            if arr[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    N = len(nums)
    for i in range(N - 1):
        t = target - nums[i]
        j = bsearch(nums[i+1:], t)
        if j != -1:
            return [i, i + 1 + j]
    return []

