# 문자열 변수 선언
str_var = "This is my python code."
multi_line = """I'm a developer.
I use python.
Thank you."""

print(str_var)
print(multi_line)

# 문자열 더하기
num1 = "12"
num2 = "24"
print(num1 + num2)
print(num1 * 3) # 121212

# 인덱싱
print(str_var[6])
print(str_var[-1]) # 없어서 . 출력

# 슬라이스
print(str_var[2:7])

str_var = str_var.replace("my", "your")
print(str_var)

# format
weather = 12.3
temp = 13
res = "{0} / {1}도 입니다.".format(weather, temp)
print(res)

# 입력
num = input(" 숫자 입력")
print(num)