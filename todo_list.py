todo_list = []

while True:
    print("")
    print("할일")
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 할 일 목록 보기")
    print("4. 종료")
    
    choice = input("선택: ")
    
    if choice == "1":
        todo = input("추가할 일 :")
        todo_list.append(todo)
        print(f"{todo} 할일이 추가되었습니다.")
        pass
    elif choice == "2":
        todo = input("삭제할 일:")
        todo_list.remove(todo)
        print(f"{todo} 할 일이 삭제되었습니다.")
        pass
    elif choice == "3":
        print(todo_list)
        pass
    else:
        print("올바른 선택이 아닙니다.")