while True:
    try:
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        result = num1 / num2
        print(f"{num1}을 {num2}로 나눈 결과는 {result}입니다.")
    except ValueError:
        print("유효한 숫자를 입력해주세요.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except Exception as e:
        print(f"예기치 못한 오류가 발생했습니다: {e}")
    else:
        print("연산이 성공적으로 완료되었습니다.")
    finally:
        print("프로그램을 종료합니다.")
        break
