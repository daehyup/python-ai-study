from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
    
    @abstractmethod
    def introduce(self):
        pass


    def hello(self):
        print(f"Hello, I am a {self.name} and I am {self.age} years old.")
    
class Human(Person):
    def introduce(self):
        print(f"I'm {self.name}, a {self.job if self.job else 'person'}, and I'm {self.age} years old.")


if __name__== "__main__":
    man = Human("John", 30, job='developer')
    man.hello()
    man.introduce()