class Solution:
    def generateParenthesis(self, n):
        result = []
        op = 0
        cl = 0
        k=""
        def generate_par(k, op, cl):
            if op == n and cl == n:
                result.append(k)
                return
            if op < n:
                k = k + "("
                generate_par(k, op +1, cl)
            if cl < op:
                k = k + ")"
                generate_par(k, op, cl +1)

        generate_par(k,op,cl)

        return result




n = 3
obj = Solution()
print(obj.generateParenthesis(n))


