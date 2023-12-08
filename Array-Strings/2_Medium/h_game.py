class Solution:
    def hIndex(self, citations: [int]) -> int:
        """
        Main Idea:
        - Sort the input array.
        - As we have a sorted array, a intuitive idea is to perform a binary search.
        """
        citations.sort()
        left = 0
        right = len(citations) - 1
        h = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= len(citations) - mid:
                h = max(h, len(citations) - mid)
                right = mid - 1
            else:
                left = mid + 1

        return h


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    s = Solution()
    print(s.hIndex(citations))
