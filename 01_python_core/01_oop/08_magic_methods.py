# 08_magic_methods.py
# 학습일: 2026-06-24
# 개념: 매직 메서드 - __str__, __repr__, __eq__, __len__

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"User({self.name})"
    
    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})"
    
    def __eq__(self, other) -> bool:
        return self.email == other.email
    
    def __len__(self) -> int:
        return len(self.name)
    
u1 = User("김철수", "cs@gmail.com")
u2 = User("이철수", "cs@gmail.com")
u3 = User("박민준", "mj@gmail.com")

print(u1)           # User(김철수)
print(repr(u1))     # User(name='김철수', email='cs@gmail.com')
print(u1 == u2)     # True  ← 이메일 같음
print(u1 == u3)     # False ← 이메일 다름
print(len(u1))      # 3     ← 김철수 3글자