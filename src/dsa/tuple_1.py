def flatten(t):
    result = []
    for item in t:
        if isinstance(item, tuple):
            result.extend(flatten(item))   # recurse into nested tuple
        else:
            result.append(item)            # base case: plain value
    return result

t = (50, (40, (50, 60)), (((70, 80, 90))))


print(flatten(t))

t1 = (70,(80,90))
print(list(t1))