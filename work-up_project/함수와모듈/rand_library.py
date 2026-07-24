import random

for i in range(1, 5):
    print(random.randint(1, 100))

basket = ["apple", "banana", "cherry"]
random_fruit = random.choice(basket)
print(random_fruit)