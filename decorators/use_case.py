from decorators import say_twice, calculate_time


@say_twice
def say():
    print("hello")

@say_twice
def greet(name):
    print(f"Hello, {name}!")

@say_twice
def farewell(name):
    print(f"Goodbye, {name}!")
    return f"Farewell, {name}!"

@calculate_time
def waste_time(num):
    for _ in range(num):
        sum([num**2 for num in range(num)])



if __name__ == "__main__":
    say()
    greet("Alice")
    farewell=farewell("Bob")
    print(farewell)  
    waste_time(10000)
    waste_time(2)