import bisect
from typing import List
from collections import Counter, defaultdict, OrderedDict

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def findLargestFactor(a, b):
            while b != 0:
                a, b = b, a%b
            return a
        def findSmallestMultiplier(nums):
            res = 1
            for num in nums:
                res = res*num//findLargestFactor(res, num)
            return res
        def findAllFactor(num):
            res = []
            for i in range(1, num+1):
                if num%i == 0:
                    res.append(i)
            return res
        print(findAllFactor(findSmallestMultiplier([12,3,6,9,18,10])))
        
    
res = Solution().findKthSmallest([3,6,9], 3)
print('Output: ', res)
print('-----------------')

