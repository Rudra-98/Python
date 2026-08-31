l = [1,2,3,4,5,6,7,8,9,11,12,13]

prime_num = []

for i in range(0,len(l)):
    if l[i] <=2:
        prime_num.append(l[i])
    else:
        is_prime = True
        for j in range(2,i):
            if l[i]%j == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(l[i])
print(prime_num)