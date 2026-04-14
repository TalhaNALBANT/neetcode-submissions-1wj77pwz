class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}

        for i,n in enumerate(nums): 
            difference = target - n
            if difference in tempMap:
                return [tempMap[difference],i]
            tempMap[n]=i


        