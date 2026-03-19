while True:
    try:
        num1 = int(input("첫번째 입력: "))
        num2 = int(input("두번째 입력: "))
        result = num1 / num2
        print(f"나누기 결과는 {result} 입니다.")
        break
    except ValueError:
        print(f"정상적인 숫자를 입력")
        continue
    except ZeroDivisionError:
        print("0으로 못 나눔")
        continue
    except:
        pass