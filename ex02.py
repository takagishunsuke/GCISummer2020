#uncoding=utf-8
#英語の成績を取得する
English_Scores = int(input("英語の成績を入力してください> "))
#数学の成績を取得する
Math_Scores = int(input("数学の成績を入力してください> "))
#英語の成績を表示する
print ("英語の点数：" + str(English_Scores))
#数学の成績を表示する
print ("数学の点数：" + str(Math_Scores))
#両教科の合計を表示する
print("合　計：" + str(English_Scores + Math_Scores))
#すべての科目を足した後、割ることで平均を表示する
print("平　均：" + str(English_Scores + Math_Scores / 2))
