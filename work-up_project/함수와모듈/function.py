def func(name):
    print(f"Hello, {name}!")

func("Alice")

def sum(a, b):
    return a + b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

result = sum(3, 5)
print(f"Sum: {result}")