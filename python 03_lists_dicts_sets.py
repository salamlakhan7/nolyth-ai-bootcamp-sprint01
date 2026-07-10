# 03_lists_dicts_sets.py
# Sprint 01
# Day 1: Python Fundamentals - Lists, Dictionaries, Sets


# ----- LISTS -----

# 1. Add and remove elements from a list
def list_add_remove():
    fruits = ["apple", "banana", "cherry"]
    fruits.append("mango")
    fruits.remove("banana")
    return fruits


# 2. Find the second largest number in a list
def second_largest(numbers):
    unique_sorted = sorted(set(numbers), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None


# 3. Reverse a list without using reverse()
def reverse_list(items):
    return items[::-1]


# 4. Count occurrences of an element in a list
def count_occurrences(items, target):
    return items.count(target)


# 5. Flatten a nested list
def flatten_list(nested):
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat


# 6. Remove duplicates from a list while keeping order
def remove_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


# 7. Merge two lists into one sorted list
def merge_sorted(list1, list2):
    return sorted(list1 + list2)


# 8. List slicing practice - get middle elements
def get_middle(items):
    return items[1:-1]


# 9. Sum and average of a list
def sum_and_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg


# 10. List comprehension - squares of even numbers
def squares_of_evens(numbers):
    return [n ** 2 for n in numbers if n % 2 == 0]


# ----- DICTIONARIES -----

# 11. Create a dictionary and update a value
def dict_add_update():
    student = {"name": "Abdul", "age": 23}
    student["city"] = "Ghotki"
    student["age"] = 24
    return student


# 12. Merge two dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


# 13. Find the key with the maximum value
def key_with_max_value(data):
    return max(data, key=data.get)


# 14. Invert a dictionary (swap keys and values)
def invert_dict(data):
    return {value: key for key, value in data.items()}


# 15. Count word frequency in a sentence
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


# 16. Filter dictionary by value condition
def filter_by_value(data, min_value):
    return {k: v for k, v in data.items() if v >= min_value}


# ----- SETS -----

# 17. Find common elements between two lists using sets
def common_elements(list1, list2):
    return set(list1) & set(list2)


# 18. Find unique elements only in one list (not in both)
def unique_to_first(list1, list2):
    return set(list1) - set(list2)


# 19. Union of two sets
def union_sets(set1, set2):
    return set1 | set2


# 20. Check if one set is a subset of another
def is_subset(small_set, big_set):
    return small_set.issubset(big_set)


# ----- Test calls -----
if __name__ == "__main__":
    print(list_add_remove())
    print(second_largest([4, 9, 2, 9, 7, 1]))
    print(reverse_list([1, 2, 3, 4, 5]))
    print(count_occurrences([1, 2, 2, 3, 2], 2))
    print(flatten_list([[1, 2], [3, 4], [5]]))
    print(remove_duplicates([1, 2, 2, 3, 1, 4]))
    print(merge_sorted([5, 1, 3], [4, 2, 6]))
    print(get_middle([1, 2, 3, 4, 5]))
    print(sum_and_average([10, 20, 30]))
    print(squares_of_evens([1, 2, 3, 4, 5, 6]))

    print(dict_add_update())
    print(merge_dicts({"a": 1}, {"b": 2}))
    print(key_with_max_value({"a": 10, "b": 25, "c": 15}))
    print(invert_dict({"a": 1, "b": 2}))
    print(word_frequency("the quick brown fox the fox runs"))
    print(filter_by_value({"a": 5, "b": 15, "c": 25}, 10))

    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    print(unique_to_first([1, 2, 3], [2, 3, 4]))
    print(union_sets({1, 2}, {2, 3}))
    print(is_subset({1, 2}, {1, 2, 3, 4}))


# OutPuts
# ['apple', 'cherry', 'mango']
# 7
# [5, 4, 3, 2, 1]
# 3
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5, 6]
# [2, 3, 4]
# (60, 20.0)
# [4, 16, 36]
# {'name': 'Abdul', 'age': 24, 'city': 'Ghotki'}
# {'a': 1, 'b': 2}
# b
# {1: 'a', 2: 'b'}
# {'the': 2, 'quick': 1, 'brown': 1, 'fox': 2, 'runs': 1}
# {'b': 15, 'c': 25}
# {3, 4}
# {1}
# {1, 2, 3}
# True


# ** Process exited - Return Code: 0 **
