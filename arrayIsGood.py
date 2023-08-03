class Solution:
    """Class check if array is good"""

    def isGood(self, nums):
        """Function returns true if the given array is good, otherwise return false.
        
        nums: list of int numbers"""
        isGood = False
        if len(nums) - max(nums) == 1:
            if nums.count(max(nums)) == 2:
                isGood = True
                for i in range(1, max(nums)):
                    if nums.count(i) == 1:
                        isGood = True
                    else:
                        isGood = False
                        break
        return isGood




