class Solution:
    def jump(self, nums: [int]) -> int:
        """
        Main Idea:
        - This problem has the same idea as jump_game.py
        - If position P is reachable, then every position before P is also reachable.
        - Therefore, at each index, we can apply memoization to calculate the maximum
        position can be reached up to that index.
        """

        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + i, nums[i - 1])
        
        target = 0
        count = 0
        while target < len(nums) - 1:
            count += 1
            target = nums[target]

        return count


if __name__ == "__main__":
    nums1 = [2, 3, 0, 1, 4]
    nums2 = [2, 3, 1, 1, 4]
    s = Solution()
    assert (s.jump(nums1) == 2)
    assert (s.jump(nums2) == 2)
    print("All Passed!!!")
