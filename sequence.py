# 奇数
def odd(n):
    print(2*n - 1)

# 偶数
def even(n):
    print(2*n)


# 次の問いに答えよ。
# (1) 一般項が an=3n−1 の数列 {an} の初項から第５項までを答えよ。

def seq(n):
    print(3*n - 1)

i = 1
while i < 5:
    seq(i)
    i += 1

# # 等差数列
# 次の数列の一般項と第５項を求めよ。
# (1) 初項が 1、公差が 3
def one(n):
    print(3*n - 2)
one(5)

# (2) 公差が 2、第10項が 23
def two(n):
    print(2*n + 3)
two(5)

# (3) 初項が 50、第10項が 23
def three(n):
    print(-3*n + 53)
three(5)

# (4) 第4項が 7、第10項が −5
def four(n):
    print(-2*n + 15)
four(5)

# 等差数列の差
# a = 初項、l = 末項、n = 項数
def five(a, l, n):
    print(1/2*n * (a + l))

# l = a + (n - 1) * dを代入すると
# a = 初項、d = 公差、n = 項数
def six(a, d, n):
    print(1/2*n * (2*a + (n - 1) * d))

five(7, 23, 8)
six(2, 3, 10)

# # フィボナッチ数
# 第0項が0、第1項が1から始まる
# 第n+2項=第n項+第n+1項になっている数列
# 例　0 1 1 2 3 5 8 13 21....

def fib(n):
    a, b =0, 1
    for t in range(0, n+1):
        print(a)
        a, b = b, a+b
    print() # 最後に改行が入る
fib(10)



# # 素数判定プログラム
n = int(input("素数判定したい3以上の数字を入力。n=:"))
for k in range(2,n):
    if n % k == 0:
        print(f"{n}は約数{k}を持つため素数ではありません")
        break
else:
    print(str(n) + "素数です")

# # 約数列挙
n = int(input("約数判定したい2以上の自然数nを入力。n=:"))
p = 0 # 約数のカウンター
for k in range(1,n+1):
    if n % k == 0:
        print(f'{n}は{k}を約数にもつ')
        p += 1
print(f"{p}個約数を持つ")

#  1から50までの自然数の和
i = 0
k = 0
for i in range(0,50):
    k = k + i + 1
print(k)

# 1から100までの偶数の和
i = 0
k = 0
for i in range(0,50):
    k = k + 2*(i + 1)
print(k)

# 2桁の3の倍数の和
i = 0
k = 0
for i in range(3,33):
    k = k + 3*(i + 1)
print(k)

# 1から50までの自然数のうち、５の倍数でない数列の和
i = 0
k = 0
for i in range(0,50): #1から50の和
    k = k + i + 1
i = 0
for i in range(0,10): #5の倍数を引く
    k = k - 5*(i + 1)
print(k)