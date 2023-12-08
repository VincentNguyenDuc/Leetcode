class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        pre = 1
        post = 1
        length = len(nums)
        sol = [1 for _ in range(length)]
        for i in range(length):
            sol[i] *= pre
            pre *= nums[i]

            sol[length - i - 1] *= post
            post *= nums[length - i - 1]

        return sol


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
