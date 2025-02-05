from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    # Write your code here
    def fetch_pairs(arr, t):
        ans = list()
        N = len(arr)
        for i in range(N):
            for j in range(i+1, N):
                if arr[i] + arr[j] == t:
                    ans.append([arr[i], arr[j]])
        return ans
    N = len(nums)
    seen = set()
    for i in range(N-2):
        t = -nums[i]
        ret = fetch_pairs(nums[i+1:], t)
        print(i, t, ret)
        if len(ret) > 0:
            for item in ret:
                seen.add(tuple(sorted([nums[i]] + item)))
    return [list(item) for item in seen]


