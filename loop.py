for i in range(5): # 0 ~ 4
    print(i)
    
for i in range(1, 5): # 1 ~ 4
    print(i)    
    
for i in range(5):
    print(i)
else:
    print("반복이 완료")
    
fruits = ["사과", "딸기", "복숭아", "참외"]

for fruit in fruits:
    print(f"{fruit}이(가) 과일 바구니에 있습니다.")
    
while True:
    user_input = input("명령어를 입력")
    if user_input == "exit":
        break
    else:
        pass

for x in range(1, 10):
    for y in range(1, 10):
        print(f"{x} * {y} = {x * y}")    