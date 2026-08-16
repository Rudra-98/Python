s = "bbbbb"

#my window should always have unique elements.

i = 0

j = 0

a = set()

max_len = -float("inf")

while(j<len(s)):
    if s[j] not in a:
        a.add(s[j])
        max_len = max(max_len,(j-i)+1)
        j = j+1
    else:
        a.remove(s[i])
        i = i+1


print(max_len)
