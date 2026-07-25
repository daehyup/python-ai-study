# 기본 매개변수
def welcom(city, name="Guest", room=None):
    if room is None:
        room = []
    room.append(101)
    print(f"Hello, {name}! Welcome to {city}. Your room number is {room}.")

welcom("Alice")

# 키워드 인자
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

display_info(name="Alice", age=30, city="New York")

# 가변 인자 리스트
def calc_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(calc_sum(1, 2, 3, 4, 5))  # Output: 15

# 키워드 가변인자 리스트
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")