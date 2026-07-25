students = {}

while True:
    print("")
    print("1. 성적 입력하기")
    print("2. 학생 조회하기")
    print("3. 학점 조회하기")
    print("0. 종료하기")
    menu = input("메뉴 번호를 입력해주세요: ")

    if menu == "1":
        name = input("학생 이름을 입력해주세요: ")
        score = int(input("학생 점수를 입력해주세요: "))
        students[name] = int(score)
        print(f"{name} 학생의 점수 {score}이(가) 입력되었습니다.")

    elif menu == "2":
        name = input("조회할 학생 이름을 입력해주세요: ")
        if name in students:
            print(f"{name} 학생의 점수는 {students[name]}점입니다.")
        else:
            print(f"{name} 학생의 정보가 없습니다.")
    
    elif menu == "3":
        name = input("학생 이름을 입력해주세요: ")
        if name in students:
            score = [students[name]]
            if score[0] >= 90:
                grade = "A"
            elif score[0] >= 80:
                grade = "B"
            elif score[0] >= 70:
                grade = "C"
            elif score[0] >= 60:
                grade = "D"
            else:
                grade = "F"
            print(f"{name} 학생의 학점은 {grade}입니다.")
        else:
            print(f"{name} 학생의 정보가 없습니다.")

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break