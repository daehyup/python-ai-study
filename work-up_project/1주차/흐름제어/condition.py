# # 단일 조건
# value = 30

# # 이 걊이 20을 초과하는 경우, Big! 이라는 메시지를 출력
# if value > 20:
#     print("Big!")


# # 복합 조건문

# # 50보다 큰 경우 Great, 50보다 작거나 같고, 20보다 큰 경우 Big, 그렇지 않은 경우 small
# if value > 50:
#     print("Great!")
# elif value > 20:
#     print("Big!")
# else:
#     print("Small!")

# # 날씨가 흐리고, 강수확률이 70% 이상이면 비가 온다
# condition = "맑음"
# rain_rate = 0.70

# if condition is "흐림" and rain_rate >= 0.7:
#     print("비가 온다.") 
# elif condition is "흐림":
#     print("흐린 날씨입니다.")
# elif condition is "맑음" and rain_rate >= 0.7:
#     print("맑은 날씨지만, 비가 올 수 있습니다.")
# else:
#     print("맑은 날씨입니다.")


# 사용자로부터 두 개의 값을 입력받는다.
# var1 = int(input("첫 번째 값을 입력하세요: "))
# var2 = int(input("두 번째 값을 입력하세요: "))

# 첫 번째 값이 크다면, "Win", 두 번째 값이 크다면 "Lose"를 출력한다.
# 두 값이 같다면 "Draw"를 출력한다.
# if var1 > var2:
#     print("Win")
# elif var1 < var2:
#     print("Lose")
# else:
#     print("Draw")

# 점수를 입력받는다.
score = int(input("점수를 입력하세요: "))

if score <= 99 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
elif score <= 79 and score >= 70:
    grade = "C"
elif score <= 69 and score >= 60:
    grade = "D" 
elif score <= 59 and score >= 1:
    grade = "F"
else:
    grade = None

if grade is not None:
    print(f"당신의 학점은 {grade}입니다.")
