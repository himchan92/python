value = 30

if value > 40:
    print("Big!")
elif value > 20:
    print("Power!")    
else:
    print("Small")
    
condition = "맑음"
rain_rate = 0.70

if condition is "흐림" and rain_rate >= 0.70:
    print("비가 올 확률이 높습니다.")
elif condition is "흐림":
    print("날씨 많이 흐림")
    
var1 = input("첫번째 입력")
var2 = input("두번째 입력")

num_var1 = int(var1)
num_var2 = int(var2)

if num_var1 > num_var2:
    print("Win")
elif num_var1 < num_var2:
    print("Lose")
else:
    print("Draw")