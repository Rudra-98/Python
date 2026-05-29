def create_allsubsets(a):
     result = []

     subset = []
     def dfs(i):
         if i>= len(a):
             result.append(subset.copy())
             return

         subset.append(a[i])
         dfs(i+1)

         subset.pop()
         dfs(i+1)

     dfs(0)
     return result

a = [1,2,3,4]
print(create_allsubsets(a))