from ast import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(0,len(nums)):
            min_index = -1
            min_number = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] <= min_number:
                    min_index = j
                    min_number = nums[j]
            if min_index != -1:
                nums[i],nums[min_index] = nums[min_index],nums[i]
        return nums[len(nums)-k]




nums = [2,3,1,1,5,5,4]
k = 3

o = Solution()
print(o.findKthLargest(nums,k))




