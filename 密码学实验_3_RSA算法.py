
#快速幂 a * b(mod m) = ((a mod m) * (b mod m)) mod m
def quickpower(x, y, m):
    print("quick")
    ans = 1
    cnt = x
    while(y):
        if(y&1):
            ans = ((ans % n) * (cnt % n)) % n
        cnt = ((cnt % n) * (cnt % n)) % n
        y>>1
    return ans


#拓展欧几里得算法
def Ex_gcd(a, b, x, y):
    if(b == 0):
        x = 1
        y = 0
        return a, x, y
    q = Ex_gcd(b, a%b, x, y)

    t1 = x
    t2 = y
    x = t2
    y = t1 - (a / b) * t2
    return q, x, y

#欧几里得算法
def gcd(a, b):
    while(1):
        r = a % b
        if(r == 0):
            break
        else:
            a = b
            b = r
    return b

#为目标寻找 最小互质数
def coprime(x):
    for i in range(2, x):
        if(gcd(i, x) == 1):
            return i
    print("居然没有互质数？不可能滴！")

def encryption(m, e, n):
    c = quickpower(m, e, n)
    print(c)
    return c

def decode(c, d, n):
    m = quickpower(c, d, n)

if __name__ ==  "__main__":
    print("欢迎使用精品RSA加密")
    print("请输入两个大素数（别真的特别大 11 23就不错！）")
    p = int(input("\n第一个大素数"))
    q = int(input("\n第二个大素数"))
    n = p * q
    fai_n = (p - 1) * (q - 1)
    e = coprime(fai_n)
    r, x, y = Ex_gcd(e, fai_n, x = 0, y = 0)
    d = (x + fai_n) % n
    print("0->退出     1->加密     2->解密 （输入0 | 1 | 2）")
    while(1):
        flag = input("\n你的选择\n")

        if(flag == "0"):
            print("感谢使用本产品！")
            break
        if(flag == "1"):
            print("请以ASCII形式输入明文: \n")
            m = int(input())
            print("OK")
            print("密文： c = " + encryption(m, e, n))
        if(flag == "2"):
            print("请以ASCII形式输入密文: \n")
            c = int(input())
            print("明文 m = " + decode(c, d, n))
        else:
            print("\n\n  非法输入\n\n")
    













    
        
