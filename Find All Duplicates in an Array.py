class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        keys = [key for key,values in dic.items() if values==2]
        return keys