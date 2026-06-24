# 06_static_class_method.py
# 학습일: 2026-06-24
# 개념: @staticmethod, @classmethod

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    @staticmethod
    def validate_email(email: str) -> bool:
        # 인스턴스 없이 호출 가능
        return "@" in email
    
    @classmethod
    def from_string(cls, data: str) -> "User":
        name, email = data.split(",")
        return cls(name, email)

# 정적 메서드 — 인스턴스 없이 호출
print(User.validate_email("cs@gmail.com"))  # True
print(User.validate_email("invalid"))        # False

# 클래스 메서드 — 문자열로 User 생성
u = User.from_string("김철수,cs@gmail.com")
print(u.name)   # 김철수
print(u.email)  # cs@gmail.com