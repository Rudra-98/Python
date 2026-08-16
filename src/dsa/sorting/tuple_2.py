def flatten_iterative(t):
    stack = list(t)[::-1]
    result = []
    while stack:
        item = stack.pop()
        if isinstance(item, tuple):
            stack.extend(item[::-1])
        else:
            result.append(item)
    return result


t = (50, (40, (50, 60)), (((70, 80, 90))))
print(flatten_iterative(t))