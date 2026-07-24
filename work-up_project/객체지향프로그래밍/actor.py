from person import Person

class Actor(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age, job="Actor")
        self.film = film
    
    def introduce(self):
        super().hello()
        print(f"Hello, I am {self.name}, a {self.age}-year-old actor. I starred in the film '{self.film}'.")