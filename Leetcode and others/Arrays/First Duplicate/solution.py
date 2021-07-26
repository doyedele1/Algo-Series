class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen: return nums[i]
            
            else: seen.add(nums[i])