class Solution:
    def reverse(self, nums: [int], left:int, right:int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
        print(nums)
            
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s.rotate(nums, k)
    
        