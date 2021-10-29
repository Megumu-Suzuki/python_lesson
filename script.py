def add_world(word):
    print(word + 'World')
# インデントはスペース4つ
add_world('Hello')


apple = 100
money = 300
input_count = input("リンゴを何個買うかを入力してください:")
# int()データ型変更　int = 整数, str = 文字列
count = int(input_count)
total_price = apple * count
if total_price < money:
    print("合計" + str(total_price) + "円です")
    print("残高は" + str(money - total_price) + "円です")
elif total_price == money:
    print("合計" + str(total_price) + "円です")
    print("残高はありません")
else:
    print(str(total_price - money) + "円足りませんでした")
    print("りんごを買えませんでした")
