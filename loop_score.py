students = {}

while True:
    # 메뉴 출력
    print("")
    print("1. 성적 입력")
    print("2. 학생 조회")
    print("3. 학점 조회")
    print("0. 종료하기")
    menu = input("메뉴 번호를 입력하세요: ")
    
    # 1. 성적 입력
    if menu == "1":
        name = input("학생 이름 입력")
        score = input("점수 입력")
        
        students[name] = int(score)
        print(f"{students[name]}의 성적은 {students[name]} 입니다.")
        pass
    
    # 2. 학생 조회
    elif menu == "2":
        name = input("조회하고자 하는 학생의 이름을 입력.")
        if name in students.keys():
            print(f"{name}의 점수는 {students[name]} 입니다.")
        else:
            print(f"{name}은 등록되지 않았습니다.")
            pass
    
    # 3. 학점 조회
    elif menu == "3":
        if name  not in students.keys():
            print(f"{name}은 등록되지 않았습니다.")
            continue
        score = students[name]
    
    # 0. 종료 하기
    elif menu == "0":
        break
    
    else:
        print("메뉴 잘못입력")        
    pass