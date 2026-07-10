# 02_loops.py
# Sprint 01
# Day 1: Python Fundamentals - Loops


# 1. Print numbers 1 to 10 using a for loop
def print_numbers():
    for i in range(1, 11):
        print(i)


# 2. Sum of numbers from 1 to n using a while loop
def sum_up_to_n(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


# 3. Print only even numbers from a list
def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)


# 4. Reverse a string using a loop
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


# 5. Count occurrences of each character in a string
def count_characters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


# 6. Multiplication table for a given number
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# 7. Find all prime numbers up to n
def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# 8. Nested loop - print a simple pattern (right triangle of stars)
def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()


# 9. Loop with break - find first number divisible by both 3 and 5
def find_first_divisible(numbers):
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            return num
    return None


# 10. Loop with continue - print only odd numbers, skip even
def print_odd_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            continue
        print(num)


# ----- Test calls -----
if __name__ == "__main__":
    print_numbers()
    print(sum_up_to_n(10))
    print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(reverse_string("Abdul"))
    print(count_characters("banana"))
    multiplication_table(5)
    print(find_primes(30))
    print_star_pattern(5)
    print(find_first_divisible([1, 4, 6, 9, 15, 20]))
    print_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



# OutPuts
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 55
# 2
# 4
# 6
# 8
# 10
# ludbA
# {'b': 1, 'a': 3, 'n': 2}
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# *
# **
# ***
# ****
# *****
# 15
# 1
# 3
# 5
# 7
# 9


# ** Process exited - Return Code: 0 **
