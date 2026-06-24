# 02_class_variables.py
# 학습일: 2026-06-24
# 개념: 클래스 변수 vs 인스턴스 변수

class User:
    user_count = 0

    def __init__(self, name: str):
        self.name = name
        User.user_count += 1

    def greet(self) -> str:
        return f"Hello, {self.name}입니다."
    
    def get_info(self) -> str:
        return f"이름: {self.name}"

user1 = User("김철수")
user2 = User("이영희")
user3 = User("박민수")

# 인스턴스 변수는 각자 다름
print(user1.name)
print(user2.name)

# 클래스 변수는 모두 공유
print(User.user_count)
print(user1.user_count)
print(user2.user_count)
print(User.user_count)