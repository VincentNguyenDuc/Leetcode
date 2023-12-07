class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        # Keep going and place non-val elements into the position
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
                
        return index
        
            
            
    
if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 2]
    val = 2
    print(s.removeElement(nums, val))