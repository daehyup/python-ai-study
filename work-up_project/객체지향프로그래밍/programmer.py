from person import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job="Programmer")
        self.language = language
    
    def introduce(self):
        print(f"Hello, I am a {self.name}, I am {self.age} years old, and I program in {self.language}.")