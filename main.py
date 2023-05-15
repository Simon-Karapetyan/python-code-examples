x = 10
y = 20
print(x + y)



fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



i = 0
while i < 10:
    print(i)
    i += 1


def print_arguments(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(key, ":", value)

print_arguments("apple", "banana", "cherry", color="red", taste="sweet")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
area = rect.area()
perimeter = rect.perimeter()

print(area) # 15
print(perimeter) # 16


Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("The dog barks: Woof!")

    def fetch(self):
        print("The dog fetches a ball.")


from functions import get_date
print(get_date())
