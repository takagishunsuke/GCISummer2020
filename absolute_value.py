#uncoding=utf-8
#xの絶対値を求める
#絶対値の出し方は、正の整数であればそのまま
#0であれば、絶対値は0
#負の整数であれば、-を削除する
#起こりうる可能性の少ないものから順番に条件を書いて、多いものはelseでカバーする

x = int(input("絶対値を求めたい数値を入力してください: "))
if x < 0:
    #yを出力する数値にする
    y = x * -1
elif x == 0:
    y = 0
else:
    y = x
print(str(x) + "の自然数は" + str(y) + "です")
