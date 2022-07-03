class Mammal:

    def walk(self):
        print("walk")


class Dog(Mammal):

    def bark(self):
        print("Dog Barks")


class Cat(Mammal):

    def annoying_cat(self):
        print("Annoying Cat")


animal1 = Dog()
animal1.bark()
animal2 = Cat()
animal2.walk()
