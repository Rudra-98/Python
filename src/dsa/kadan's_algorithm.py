from hmac import new


class kadane:
    def maximum_subarray(self, nums):
        r = 0
        max_sum = 0
        while nums[r] < -1:
            r += 1
            curr_sum = 0
        new_list = nums[r:]
        if len(new_list) ==0:
            new_list = nums
        l = 1
        curr_sum = new_list[0]
        while l < len(new_list):
            if curr_sum < -1:
                curr_sum = new_list[l]
            else:
                curr_sum += new_list[l]
            max_sum = max(curr_sum, max_sum)
            l = l + 1

        return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
o = kadane()
print(o.maximum_subarray(nums))







