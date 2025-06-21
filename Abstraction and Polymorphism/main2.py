from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run as a human")

class Snake(Animal):
    def move(self):
        print("I can crawl as a snake")

class Dog(Animal):
    def move(self):
        print("I can bark as a dog")

class Lion(Animal):
    def move(self):
        print("I can roar and hunt as a lion")

R = Human()

K = Snake()

A = Dog()

B = Lion()

for an in(R,K,A,B):
    an.move()

gib = int(input("Enter what class fr specific like Human Snake Dog or Lion:  "))

if gib == "Human":
    R.move()
elif gib == "Snake":
    K.move()
elif gib == "Dog":
    A.move
else:
    B.move