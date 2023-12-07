class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        # Very similar to remove_element.py
        # The only difference is that instead of comparing with a specific value
        # We compare with the current element at index
        # This is due to the fact that the input array is already sorted
        index = 0
        for num in nums:
            if index == 0 or nums[index - 1] != num:
                nums[index] = num
                index += 1
                
        return index