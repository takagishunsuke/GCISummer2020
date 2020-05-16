#uncoding=utf-8
#アセットを入力してもらう
m = float(input("身長をm単位で入力して下さい> "))
kg = int(input("体重をkg単位で入力して下さい> "))

#BMIを求める関数をつく
def show_BMI(m,kg):
    BMI = kg / (m*m)
    return BMI

#入力してもらった数字をもとに、BMIを表示する
usersBMI = show_BMI(m,kg)

print("あなたのBMIは：" + str(usersBMI))
