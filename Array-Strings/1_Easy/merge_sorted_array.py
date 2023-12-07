class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        
        # We use 3 pointers
        i1 = m - 1 # The end of elements in nums1
        i2 = n - 1 # The end of elements in nums2
        final_i = m + n - 1 # The end of length of nums1
        
        # Go from the back, and place the largest element at the decreasing index final_i
        while i2 >= 0:
            if i1 >= 0 and nums1[i1] >= nums2[i2]:
                nums1[final_i] = nums1[i1]
                i1 -= 1
            else:
                nums1[final_i] = nums2[i2]
                i2 -= 1
            final_i -= 1

        print(nums1)
            
        
if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,4,0,0,0]
    m = 4
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
                
        