class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            index = start + ((end - start)//2)
            if target < nums[index]:
                end = index -1
            elif target > nums[index]:
                start = index + 1
            else:
                return index
        return -1
            
