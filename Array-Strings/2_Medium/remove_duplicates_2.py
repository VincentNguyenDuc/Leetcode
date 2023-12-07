class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        # This is an extended problem from remove_duplicates.py
        # Instead of checking with the element right before it,
        # We check with the element 2 steps before it
        index = 0
        for num in nums:
            if index == 0 or index == 1 or nums[index - 2] != num:
                nums[index] = num
                index += 1
                
        return index
    
if __name__ == "__main__":
    s = Solution()
    nums1 = [1,1,1,2,2,3]
    print(s.removeDuplicates(nums1) == 5)
    
    nums2 = [0,0,1,1,1,1,2,3,3]
    print(s.removeDuplicates(nums2) == 7)