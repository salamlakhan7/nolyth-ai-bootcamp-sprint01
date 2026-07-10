# 01_functions.py
# Sprint 01 
# Day 1: Python Fundamentals - Functions


def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


def is_even(n):
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0


def greet(name, greeting="Hello"):
    """Returns a greeting string using a default parameter."""
    return f"{greeting}, {name}!"


def sum_all(*args):
    """Accepts any number of arguments, returns their total."""
    return sum(args)


def describe_person(**kwargs):
    """Accepts keyword arguments and prints them formatted."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def find_max(numbers):
    """Returns the largest value in a list without using max()."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def is_palindrome(text):
    """Returns True if a string reads the same backward, ignoring case."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def factorial(n):
    """Returns n! using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def count_vowels(text):
    """Returns how many vowels are in a given string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def safe_divide(a, b):
    """Returns division result, or None with a message if dividing by zero."""
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b


# ----- Test calls -----
if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(is_even(10))
    print(greet("Abdul"))
    print(greet("Abdul", "Welcome"))
    print(sum_all(1, 2, 3, 4, 5))
    describe_person(name="Abdul", age=23, city="Ghotki")
    print(find_max([4, 9, 2, 7, 1]))
    print(is_palindrome("Madam"))
    print(is_palindrome("Hello"))
    print(factorial(5))
    print(count_vowels("Sprint01 Backend Foundations"))
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))


# OutPuts 
# 8
# True
# Hello, Abdul!
# Welcome, Abdul!
# 15
# name: Abdul
# age: 23
# city: Ghotki
# 9
# True
# False
# 120
# 8
# 5.0
# Error: Cannot divide by zero.
# None


# ** Process exited - Return Code: 0 **
