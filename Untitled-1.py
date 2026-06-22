# add_10 = lambda x: x + 10

# num = int(input("Enter an integer: "))
# print("Result after adding 10:", add_10(num))

# square = lambda x: x * x
# cube = lambda x: x * x * x

# num = int(input("Enter a number: "))
# print("Square:", square(num))
# print("Cube:", cube(num))

# last_char = lambda s: s[-1]

# text = input("Enter a string: ")
# print("Last character:", last_char(text))

# palindrome = lambda s: s == s[::-1]

# s = input("Enter a string: ")

# if palindrome(s):
#     print("The string is Palindrome")
# else:
#     print("The string is NOT Palindrome")

# check_char = lambda s, ch: ch in s

# s = input("Enter a string: ")
# ch = input("Enter a character: ")

# if check_char(s, ch):
#     print("Character is present in the string")
# else:
#     print("Character is NOT present in the string")

# sum_n = lambda n: sum(range(1, n + 1))

# n = int(input("Enter n: "))
# print("Sum till n =", sum_n(n))

# last_n = lambda lst, n: lst[-n:]

# lst = [10, 20, 30, 40, 50]
# n = int(input("Enter n: "))

# print("Last n elements:", last_n(lst, n))

# result = lambda ch: ord(ch) if ch.islower() else str(ord(ch))[::-1]

# ch = input("Enter a character: ")

# print("Result:", result(ch))

# import keyword

# is_keyword = lambda s: keyword.iskeyword(s)

# s = input("Enter a string: ")

# if is_keyword(s):
#     print("It is a Keyword")
# else:
#     print("It is NOT a Keyword")  

# list_ = [1, 2, 3, 4]

# out = list(map(lambda i: [i*i, i*i*i], list_))

# print(out)  
import numpy as np
arr = np.arange(1 , 21).reshape(5,4)
print(arr)

