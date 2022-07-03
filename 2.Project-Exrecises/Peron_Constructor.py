from unicodedata import name


class Person:

    # def name(self):
    #     name = input("Name: ")
    #     print(name)

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} wants to talk")


naam = input("Name: ")
person1 = Person(naam)
person1.talk()
