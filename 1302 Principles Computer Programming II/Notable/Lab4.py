# Tribonacci Calculator: Function developling to calcuate a value's tribonacci properties

res = {}

def tribonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in res:
        return res[n]
    ans = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    res[n] = ans
    return ans


print(tribonacci(int(input('Number: '))))
