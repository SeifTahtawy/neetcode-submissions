from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequencyMap = defaultdict(int)
        buckets = [[] for _ in range(n+1)]
        ans = []

        for num in nums:
            frequencyMap[num] += 1
        
        for num in frequencyMap:
            buckets[frequencyMap[num]].append(num)
        

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                k -= 1
                if k == 0:
                    return ans
        
        return ans


        