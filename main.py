def checker(function):
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have a problem: {exc}")
        else:
            print(f"No problems. Result - {result}")

    return wrapper

@checker
def calculate(expression):
    return eval(expression)

# Приклади використання

num1 = "2 + 2"
calculate(num1)  # Виведе: No problems. Result - 4

num2 = "10 / 0"
calculate(num2)  # Виведе: We have a problem: division by zero

num3 = "10 +"
calculate(num3)  # Виведе: We have a problem: unexpected EOF while parsing

num4 = "2 + a"
calculate(num4)  # Виведе: We have a problem: name 'a' is not defined

num5 = ""
calculate(num5)  # Виведе: We have a problem: unexpected EOF while parsing
