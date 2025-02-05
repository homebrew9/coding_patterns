from typing import List

def largest_container(heights: List[int]) -> int:
    # Write your code here
    N = len(heights)
    left, right = 0, N - 1
    res = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        res = max(res, area)
        if heights[left] == heights[right]:
            left += 1
            right -= 1
        elif heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return res


