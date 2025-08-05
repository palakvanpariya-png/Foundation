# ---------------------- TASKS ----------------------

# 1. Create a list of the cubes of all numbers from 0 to 20.
cubs = [x**3 for x in range(21)]
print("Cubes:", cubs)

# 2. From a given list of integers, create a new list containing only the odd numbers.
nums = [3, 5, 4, 8, 9, 10, 11, 12, 13, 14, 15]
odds = [x for x in nums if x%2 != 0]
print("Odd numbers:", odds)

# 3. Given a list of strings, return a list with only the strings that are longer than 5 characters.
words = ["apple", "banana", "kiwi", "watermelon", "fig"]
long_words = [word for word in words if len(word) > 5]
print("Long words:", long_words)


# 4. Generate a list of all lowercase letters from a given string (ignore digits and punctuation).
text = "Hello World! 123"
letters = [ch for ch in text if ch.isalpha() and ch.islower()]
print("Lowercase letters:", letters)

# 5. Given a list of words, return a list of their lengths.
words = ["apple", "banana", "kiwi", "watermelon", "fig"]
word_lenghts = [len(x) for x in words]
print("Word lengths:", word_lenghts)

# 6. Flatten the following 2D list: [[1, 2], [3, 4], [5, 6]].
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [items for row in matrix for items in row ]
print("Flattened matrix:", flattened)

# 7. Given a list of temperatures in Celsius, convert them to Fahrenheit using the formula: F = C * 9/5 + 32.
celsius = [0, 10, 20, 30, 40]
fahrenheit = [temp*9/5+32 for temp in celsius]
print("Fahrenheit:", fahrenheit)

# 8. From a list of numbers, replace every negative number with 0.
nums_with_negatives = [-5, 3, -1, 7, 0]
new_list = [x for x in nums_with_negatives if x >= 0]
print("No negatives:", new_list)

# 9. From two lists [1, 2, 3] and [4, 5, 6], create all possible pairs as tuples.
a = [1, 2, 3]
b = [4, 5, 6]
pairs = [(x, y) for x in a for y in b]
print("All pairs:", pairs)

# 10. Extract all vowels from the string "comprehension" into a list.
sample_text = "comprehension"
vowels = [ch for ch in sample_text if ch in 'aeiou']
print("Vowels:", vowels)


# # ---------------------- SOLUTIONS ----------------------

# # 1
# cubes = [x**3 for x in range(21)]
# print("1. Cubes:", cubes)

# # 2
# nums = list(range(20))
# odds = [x for x in nums if x % 2 != 0]
# print("2. Odd numbers:", odds)

# # 3
# words = ["apple", "banana", "kiwi", "watermelon", "fig"]
# long_words = [word for word in words if len(word) > 5]
# print("3. Long words:", long_words)

# # 4
# text = "Hello World! 123"
# letters_only = [ch for ch in text if ch.isalpha() and ch.islower()]
# print("4. Lowercase letters:", letters_only)

# # 5
# word_lengths = [len(word) for word in words]
# print("5. Word lengths:", word_lengths)

# # 6
# matrix = [[1, 2], [3, 4], [5, 6]]
# flattened = [item for row in matrix for item in row]
# print("6. Flattened matrix:", flattened)

# # 7
# celsius = [0, 10, 20, 30, 40]
# fahrenheit = [temp * 9/5 + 32 for temp in celsius]
# print("7. Fahrenheit:", fahrenheit)

# # 8
# nums_with_negatives = [-5, 3, -1, 7, 0]
# no_negatives = [x if x >= 0 else 0 for x in nums_with_negatives]
# print("8. No negatives:", no_negatives)

# # 9
# a = [1, 2, 3]
# b = [4, 5, 6]
# pairs = [(x, y) for x in a for y in b]
# print("9. All pairs:", pairs)

# # 10
# sample_text = "comprehension"
# vowels = [ch for ch in sample_text if ch in 'aeiou']
# print("10. Vowels:", vowels)
