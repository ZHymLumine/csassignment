'''
两个数合并(comp):为保持唯一性，直接将两个数的二进制表示拼接在一起
默认这两个数都是32位的，拼接之后64位

decomp:将需要分解的数的前后32位分别取出作为x和y即可
x = z << 32
x = (z << 32) >> 32 这句在python中不会改变z的值(python中的数可以用无限位表示，并不会截断)
因此直接位与32个1, 即无符号int最大值2^32 - 1 = 4294967295
'''

def comp(x, y):
    res = x
    res <<= 32
    res |= y
    
    return res;


def decomp(z):
    res = [0]* 2
    x = z >> 32
    unsignedIntMax = 4294967295 #32位1
   
    y = z & unsignedIntMax
    print(y)
    
    res[0], res[1] = x, y
    return res

res = comp(3, 4)
print(res)

ans = decomp(res)
print(ans)

