class Container:
    def __init__(self, heights):
        self.heights = heights


    def find_most_water(self):
        i = 0
        j = len(self.heights) - 1
        max_water = -float('inf')
        while i < j:
            current_water = min(self.heights[i], self.heights[j])*(j-i)
            if self.heights[i] > self.heights[j]:
                j = j -1
            else:
                i = i + 1

            max_water = max(max_water, current_water)

        return max_water



height = [1,7,2,5,4,7,3,6]
o = Container(height)
print(o.find_most_water())
