list_1 = [ 3, 7 ,70, 60 , 10,90]

#selection sort

maxi = max(list_1)+1

for i in range(0,len(list_1)):
    min_i = maxi
    for j in range(i+1,len(list_1)):
        if list_1[j] < min_i:
            min_i = list_1[j]
            min_index = j
    if min_i < list_1[i]:
       list_1[i],list_1[min_index] = min_i , list_1[i]
print(list_1)