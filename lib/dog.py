#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = 'Mutt'):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed}"

snoopy = Dog("Tommy")
print(snoopy)