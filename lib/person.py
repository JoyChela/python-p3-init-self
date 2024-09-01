#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"


person1 = Person('Joy')
print(person1)