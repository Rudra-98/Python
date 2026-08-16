import heapq



from ast import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)  # discard the smallest, keep only top k
        return heap[0]

nums = [2,3,1,1,5,5,4]
k = 3

o = Solution()
print(o.findKthLargest(nums,k))
