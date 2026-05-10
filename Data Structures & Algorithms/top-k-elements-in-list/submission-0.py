class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        for i in nums:
            ans[i]+=1
        
        sorted_ans = sorted(ans.items(), key = lambda x: x[1], reverse=True)

        return [key for key, value in sorted_ans[:k]]