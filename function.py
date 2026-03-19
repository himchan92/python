# 함수 선언
def func(name):
    print(f"this is function. hello!! {name}")
    
# 함수 호출    
func("Park!!")

def sum(num1, num2):
    return num1 + num2

def div(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 / num2

result = sum(3, 5)
print(result)

result_div = div(3, 2)
print(result_div)