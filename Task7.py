class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def compare(p1, p2):
        if p1.age > p2.age:
            return True
        else:
            return False


person1 = Person('Peter', 15)
person2 = Person('Ivan', 23)
print(Person.compare(person1, person2))