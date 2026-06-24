class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "동물 소리"

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        return "멍멍!"

class Cat(Animal):
    def speak(self) -> str:
        return "야옹!"

dog = Dog("바둑이", "진돗개")
cat = Cat("나비")

print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True
print(isinstance(dog, Cat))      # False
print(isinstance(cat, Cat))      # True
print(isinstance(cat, Animal))   # True