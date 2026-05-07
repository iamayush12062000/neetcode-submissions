class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        ans = []
        for i, ele in enumerate(nums):
            find = target - ele
            if (find) in seen:
                ans.append(min(seen[find], i))
                ans.append(max(seen[find], i))
            seen[ele] = i
        return ans
