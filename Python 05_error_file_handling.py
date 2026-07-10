
# 1. Basic try/except for division by zero
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None


# 2. Handling multiple exception types
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"Error: '{value}' is not a valid number.")
        return None
    except TypeError:
        print("Error: Invalid type provided.")
        return None


# 3. try/except/else/finally - full structure
def process_number(value):
    try:
        result = 100 / value
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Processing complete.")


# 4. Custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age must be positive.")


def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    return f"Age {age} is valid."


# 5. Catching a custom exception
def validate_age(age):
    try:
        return check_age(age)
    except InvalidAgeError as e:
        return str(e)


# 6. Handling list index errors
def get_item_safe(items, index):
    try:
        return items[index]
    except IndexError:
        print("Error: Index out of range.")
        return None


# 7. Handling dictionary key errors
def get_value_safe(data, key):
    try:
        return data[key]
    except KeyError:
        print(f"Error: Key '{key}' not found.")
        return None


# ----- FILE HANDLING -----

# 8. Write to a file
def write_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


# 9. Read from a file safely (handles missing file)
def read_from_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None


# 10. Append to a file and count lines
def append_and_count_lines(filename, new_line):
    with open(filename, "a") as f:
        f.write(new_line + "\n")

    with open(filename, "r") as f:
        lines = f.readlines()
    return len(lines)


# ----- Test calls -----
if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))

    print(convert_to_int("42"))
    print(convert_to_int("abc"))

    process_number(5)
    process_number(0)

    print(validate_age(25))
    print(validate_age(-5))

    print(get_item_safe([1, 2, 3], 1))
    print(get_item_safe([1, 2, 3], 10))

    print(get_value_safe({"name": "Abdul"}, "name"))
    print(get_value_safe({"name": "Abdul"}, "age"))

    write_to_file("sample.txt", "Hello from Sprint01\nLearning file handling.")
    print(read_from_file("sample.txt"))
    print(read_from_file("missing.txt"))

    print(append_and_count_lines("sample.txt", "New line added."))


#################### Outputs ##################################
# 5.0
# Error: Cannot divide by zero.
# None
# 42
# Error: 'abc' is not a valid number.
# None
# Result: 20.0
# Processing complete.
# Cannot divide by zero.
# Processing complete.
# Age 25 is valid.
# Invalid age: -5. Age must be positive.
# 2
# Error: Index out of range.
# None
# Abdul
# Error: Key 'age' not found.
# None
# Hello from Sprint01
# Learning file handling.
# Error: File 'missing.txt' not found.
# None
# 2


# ** Process exited - Return Code: 0 **
