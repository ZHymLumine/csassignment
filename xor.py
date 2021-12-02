
'''
默认x和y都是32位的整数，每次循环将x的最后一位和y的最后一位相加模2得到对应位的
异或结果(异或是不进位的加法，这里采取mod2的方式把进位去掉)
res数组中存异或后每一位的值，遍历一遍res数组，求出最终结果

'''
def xor(x, y):  
    res = [0] * 32
    index = 0
    while(x or y):
        res[index] = ((x & 1) + (y & 1)) % 2
        index += 1
        x >>= 1
        y >>= 1
    ans = 0
    for i, n in enumerate(res):
        ans += 2 ** i * n
    return ans

#m = 12341
#n = 451214
ans = xor(m, n)


#用异或运算符^验证答案
if(ans == m ^ n):
    print("Yes")
else:
    print("No")

