# 01_class_basic.py
# 학습일: 2026-06-24
# 개념: 클래스 기초 - __init__, 인스턴스 변수, 메서드

# ========================
# 개념 1: __init__과 인스턴스 변수
# ========================
class User:
    def __init__(self, name: str, email: str):
        self.name = name # 인스턴스 변수
        self.email = email

    def greet(self) -> str:
        return f"Hello, {self.name}입니다."
    
    def get_info(self) -> str:
        return f"이름: {self.name}, 이메일: {self.email}"
    
# 실행
user1 = User("김철수", "cs@gmail.com")
user2 = User("이영희", "yh@gmail.com")

print(user1.greet())
print(user2.get_info())

