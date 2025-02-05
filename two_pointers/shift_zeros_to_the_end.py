from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    # Write your code here
    N = len(nums)
    i, j = 0, 0
    while j < N:
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
        j += 1
    while i < N:
        nums[i] = 0
        i += 1


