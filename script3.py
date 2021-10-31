# # numpy の学習

# ライブラリのインポート
import matplotlib.pyplot as plt
import numpy as np

# 等差数列
# 1〜10までの項差1
ans = np.arange(1,11,1)
print(ans)
print(sum(ans))

a = np.array([0, 1, 2, 3, 4])
b = np.array([2, 4, 6, 8, 10])
print(a)
print(b)
print(a + b)
print(a + 4)
print(b - a)
print(a * b)
print(a / b)
print(a ** b)
# # グラフとして描画するデータ
# x = np.array([1,2,3,4])
# y = np.array([2,3,4,5])

# # グラフを描画
# plt.plot(x, y)
# plt.show()