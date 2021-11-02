# 問題1
# なんとか数列

# def tri(n):
#     a, b, c=1, 0, 5
#     for t in range(0 , n+1):
#         print(a)
#         a, b, c =b, c, a+b+c
#         print()
# tri(32)

# # 問題2
# 1234567890で30000000以下の約数の合計
# n = int(input("約数判定したい2以上の自然数nを入力。n=:"))
# i=0
# for k in range(1,30000000):
#     if n % k == 0:
#         print(f'{n}は{k}を約数にもつ')
#         i = i+k
# print(i)

# # 問題3
# 3の倍数or3のつく数字の合計40000以下
# k=0
# for i in range(1, 40000):
#     if (i%3 == 0) or ('3'in str(i)):
#         k = k + i
# print(k)

# 問題4
# 面積が6000以下の直角三角形は何個？

# import math
# a = 1
# list = []
# while a**2/2 < 6000:
#     b = a + 1
#     while a*b/2 <= 6000:
#       cs = a**2 + b**2
#       c = math.floor(math.sqrt(cs) + 0.001)
#       if c**2 == cs:
#           list.append((a, b, c))
#           print(a, b, c)
#       b += 1
#     a += 1

# print(list)
# print(len(list))


#問5
# 1〜700kgの荷物積載量5000kg
p=0
c=0
for i in reversed(range(1, 701)):
    while p <= 5000:
    p = p + i
    c=c+1
print(c)