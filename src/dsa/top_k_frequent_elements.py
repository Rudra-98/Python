class Solution:
    def topKFrequent(self, nums, k):
        dict_1 = {}
        result = [[]] * (len(nums) + 1)
        final_result =[]
        for ele in nums:
            if ele in dict_1:
                dict_1[ele] = dict_1[ele] + 1
            else:
                dict_1[ele] = 1

        for key, value in dict_1.items():
            if result[value] != []:
                result[value].append(key)
            else:
                result[value]=[key]

        j = len(result)-1
        while(len(final_result) <= k):
            if result[j]:
                for u in result[j]:
                    final_result.append(u)
                    k= k-1
            j = j-1
        return  final_result


nums = [1,2,2,3,3,3]
k=2
obj = Solution()
print(obj.topKFrequent(nums, k))





