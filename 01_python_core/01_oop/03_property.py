# 03_property.py
# 학습일: 2026-06-24
# 개념: @property - getter/setter

class User:
    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("이름은 비울 수 없습니다.")
        self._name = value
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("유효한 이메일 주소가 아닙니다.")
        self._email = value

# 정상 동작 확인
u = User("김철수", "kim@example.com")
print(u.name)  # 김철수
print(u.email)  # kim@example.com

# setter 확인
u.name = "이영희"
print(u.name)  # 이영희

# ValueError 확인
try:
    u.name = ""
except ValueError as e:
    print(e)  # 이름은 비울 수 없습니다.

try:
    u.email = "invalid_email"
except ValueError as e:
    print(e)  # 유효한 이메일 주소가 아닙니다.