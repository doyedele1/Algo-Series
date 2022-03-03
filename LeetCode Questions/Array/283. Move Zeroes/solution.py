'''
    Explanation:
        [0,1,0,3,12]
        First Iteration --> [0, 1, 0, 3, 12]
                            i
                            j
        Second Iteration --> [1, 1, 0, 3, 12]
                                i
                                j
        Third Iteration --> [1, 1, 0, 3, 12]
                                    i
                                j
        Fourth Iteration --> [1, 3, 0, 3, 12]
                                        i
                                    j
        Fifth Iteration --> [1, 3, 12, 3, 12]
                                            i
                                        j
                                    
        Result ==> [1, 3, 12, 0, 0]
'''


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        for i in range(j, len(nums)):
            nums[i] = 0

        # TC - O(n)
        # SC - O(1)

        # One-line solution
        # nums[:] = [x for x in nums if x != 0] + [0]*nums.count(0)