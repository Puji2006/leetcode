class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                dup =i
        for i in range(1,len(nums)+1):
            if i not in seen:
                miss  = i
        return [dup,miss]
           