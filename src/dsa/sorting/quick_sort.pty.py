class Solution:
    def quick_sort(self, nums,s,e):
        ref = nums[s]
        p1 = s+1
        p2 = e

        while p1<=p2:
            if nums[p1]<=ref:
                p1 = p1 + 1
            elif nums[p2]>ref:
                p2 = p2 -1
            else:
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p2 = p2-1
                p1 = p1+1

        if p2<p1:
            nums[p2],nums[s] = ref,nums[p2]


        return p2



    def quick(self,A,s,e):
        if s>=e:
            return
        p = self.quick_sort(A, s, e)
        self.quick(A, s, p-1)
        self.quick(A, p+1, e)
        return A


nums = [5,3,2,9,7]
obj = Solution()
print(obj.quick(nums,0,len(nums)-1))









