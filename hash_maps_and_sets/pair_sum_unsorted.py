from typing import List
from collections import defaultdict

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    hsh = defaultdict(list)
    for i, v in enumerate(nums):
        delta = target - v
        if delta in hsh:
            # "sorted" should not be used, since index order does not matter.
            # It's incorrectly implemented in the OJ.
            return sorted([i, hsh[delta][0]])
        hsh[v] += [i]
    return []

# Main section
for nums, target in [
                       ([-1, 3, 4, 2], 3),
                    ]:
    print(f'nums, target = {nums}, {target}')
    r = pair_sum_unsorted(nums, target)
    print(f'r = {r}')
    print('==================')

