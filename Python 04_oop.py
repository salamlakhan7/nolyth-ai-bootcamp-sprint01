
# Sprint 01
# Day 2: Python Fundamentals - OOP (Classes & Inheritance)


# 1. Basic class with attributes and a method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


# 2. Class with a class variable (shared across instances)
class Counter:
    total_count = 0

    def __init__(self):
        Counter.total_count += 1


# 3. Encapsulation - private attribute with getter/setter
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount


# 4. Basic inheritance - single parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


# 5. Inheritance with super() - extending parent constructor
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def details(self):
        return f"{self.name} manages a team of {self.team_size}."


# 6. Multilevel inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range

    def info(self):
        return f"{self.brand} {self.model} - Range: {self.battery_range} km"


# 7. Multiple inheritance
class Flyable:
    def fly(self):
        return "I can fly."


class Swimmable:
    def swim(self):
        return "I can swim."


class Duck(Flyable, Swimmable):
    pass


# 8. Polymorphism - same method name, different behavior
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# 9. Method overriding
class Bird:
    def move(self):
        return "Birds can fly."


class Penguin(Bird):
    def move(self):
        return "Penguins can't fly, they swim."


# 10. Class method vs static method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def class_name(cls):
        return cls.__name__


# 11. Abstraction using an abstract-like base class (no direct instantiation logic)
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement this method.")


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."


class CashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Cash."


# 12. Operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


# 13. Composition (has-a relationship instead of is-a)
class Engine:
    def start(self):
        return "Engine started."


class CarWithEngine:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        return self.engine.start()


# 14. Checking type and instance relationships
class Student:
    def __init__(self, name):
        self.name = name


def check_instance(obj):
    return isinstance(obj, Student)


# 15. Property decorator - controlled attribute access
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


# ----- Test calls -----
if __name__ == "__main__":
    p = Person("Abdul", 23)
    print(p.introduce())

    Counter()
    Counter()
    print(Counter.total_count)

    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(300)
    print(account.get_balance())

    d = Dog("Rex")
    print(d.speak())

    m = Manager("Sara", 90000, 5)
    print(m.details())

    ec = ElectricCar("Tesla", "Model 3", 400)
    print(ec.info())

    duck = Duck()
    print(duck.fly())
    print(duck.swim())

    shapes = [Rectangle(4, 5), Circle(3)]
    for s in shapes:
        print(s.area())

    penguin = Penguin()
    print(penguin.move())

    print(MathUtils.add(4, 5))
    print(MathUtils.class_name())

    payments = [CreditCardPayment(), CashPayment()]
    for method in payments:
        print(method.pay(500))

    p1 = Point(2, 3)
    p2 = Point(4, 1)
    print(p1 + p2)

    car = CarWithEngine()
    print(car.start_car())

    s = Student("Ali")
    print(check_instance(s))

    temp = Temperature(30)
    print(temp.fahrenheit)



########################### OutPuts ###########################

# Hi, I'm Abdul and I'm 23 years old.
# 2
# 1200
# Rex barks.
# Sara manages a team of 5.
# Tesla Model 3 - Range: 400 km
# I can fly.
# I can swim.
# 20
# 28.26
# Penguins can't fly, they swim.
# 9
# MathUtils
# Paid 500 using Credit Card.
# Paid 500 using Cash.
# (6, 4)
# Engine started.
# True
# 86.0


# ** Process exited - Return Code: 0 **
