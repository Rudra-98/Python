from heapq import merge


class MergeSort(object):

    #sort the arrays
    def merge(self,A,s,m,e):
        p1 = s
        p2 = m+1
        result = [0]*(e-s+1)
        k=0
        while p1 <= m and p2 <= e:
            if A[p1] <= A[p2]:
                result[k] = nums[p1]
                k= k+1
                p1 = p1+1
            else:
                result[k] = nums[p2]
                k=k+1
                p2 = p2+1
        while p1 <= m:
            result[k] =A[p1]
            k= k+1
            p1 = p1+1
        while p2 <= e:
            result[k] = A[p2]
            p2=p2+1
            k=k+1
        y=0
        for i in range(s,e+1):
            A[i] = result[y]
            y=y+1
        return A



    def merge2(self,nums,s,e):
        if s==e:
            return
        mid = (s+e)//2
        self.merge2(nums,s,mid)
        self.merge2(nums,mid+1,e)
        c = self.merge(nums ,s ,mid,e)
        return c


nums = [45, 12, 78, 3, 90, 34, 67, 23, 89, 1, 56, 17, 72, 8, 39]
obj = MergeSort()
print(obj.merge2(nums,0,len(nums)-1))


