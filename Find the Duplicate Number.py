class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash={}
        for i,val in enumerate(nums):
            if val in hash:
                return val
            else:
                hash[val]=1
