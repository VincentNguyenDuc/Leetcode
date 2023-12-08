class Solution:
    def canJump(self, nums: [int]) -> bool:
        """Main Idea: 
        If position P is reachable, then every position before P is also reachable.
        Therefore, we only need to keep track of the maximum position that is currently reachable.
        """
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True
        


if __name__ == "__main__":
    nums1 = [3, 2, 1, 0, 4]
    nums2 = [2, 3, 1, 1, 4]
    s = Solution()
    assert(s.canJump(nums1) == False)
    assert(s.canJump(nums2) == True)
    print("All Passed!!!")
    
