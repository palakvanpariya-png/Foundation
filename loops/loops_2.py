def print_fruits():
    fruits = ["orange", "apple", "mango", "lemon"]

    for index in range(len(fruits)):
        fruit = fruits[index]

        print(f"Fruit at index {index} is {fruit}")


    # better way to do the previous code

    for index, fruit in enumerate(fruits):
        print(f"Fruit at index {index} is {fruit}")

# how to use enumerate for counting
def display_options():
    options = ["Option 1", "Option 2", "Option 3"]

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


# parallel iteration
def print_fruits_and_prices():
    fruits = ["orange", "apple", "mango", "lemon"]
    prices = [1.5, 2.0, 1.8, 1.2]

    for fruit, price in zip(fruits, prices):
        print(f"The price of {fruit} is ${price:.2f}")

def print_knock():
    for _ in range(3):
        print("knock, knock, knock")
        print("penny")

def reverse_iteration():
    actions = ["Type text", "Select text", "Cut text", "Paste text"]

    for action in reversed(actions):
        print(f"Action: {action}")

def main():
    print_fruits()
    print()
    display_options()
    print()
    print_fruits_and_prices()
    print_knock()
    reverse_iteration()

main()
    

