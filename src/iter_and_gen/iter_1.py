class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self  # returns itself as the iterator

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

# Usage
nums = CountUpTo(5)
print(nums)
print(nums)
print(nums)
print(nums)


# 1 2 3 4 5