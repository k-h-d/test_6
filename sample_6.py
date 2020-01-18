import random as rd
cnt=0

while cnt<3:
    j=input("1～10の数字入力：")
    if j.isdigit():
        a=rd.randint(1,11)
        if int(j)==a:
            print("正解")
        else:
            print("不正解")
    else:
        print("数字のみ入力")
        continue
    cnt+=1
