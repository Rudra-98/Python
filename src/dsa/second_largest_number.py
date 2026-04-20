def second_largest_number(nums):
    sorted_nums = list(set(sorted(nums)))
    if len(sorted_nums) > 1:
        return sorted_nums[len(sorted_nums) - 2]
    elif len(sorted_nums) == 1:
        return -1
    else:
        return -1



print(second_largest_number([1, 2, 3, 4, 5]))
print(second_largest_number([5, 5, 5, 5]))
print(second_largest_number([1]))
print(second_largest_number([3, 1, 4, 1, 5, 9]))
print(second_largest_number([-1, -2, -3]))
print(second_largest_number([]))