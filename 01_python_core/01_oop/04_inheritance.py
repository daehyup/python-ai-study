# 04_inheritance.py
# 학습일: 2026-06-24
# 개념: 상속, super(), 메서드 오버라이딩

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "동물 소리"
    
class Dog(Animal):
    def __init__(self, name:str, breed:str):
        super().__init__(name)
        self.breed = breed
    
    def speak(self) -> str:
        return "멍멍!"
    
    def get_info(self) -> str:
        return f"{self.name} ({self.breed})"

class Cat(Animal):
    def speak(self):
        return "야옹!"

dog = Dog("바둑이", "진돗개")
print(dog.get_info())

cat = Cat("나비")

print(dog.name)     # 바둑이
print(dog.speak())  # 멍멍!
print(cat.speak())  # 야옹!