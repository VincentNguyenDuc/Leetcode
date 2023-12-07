class Solution:
    def majorityElement(self, nums: [int]) -> int:
        # Intuitive solution: use a dict to count the occurences of elements
        # Even though it has linear time complexity, this is not O(1) in terms of space complexity
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
                
if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))