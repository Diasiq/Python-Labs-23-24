class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname 

    def __str__(self):
        return self.name + self.surname
    
person = Person("Linus", "Torvalds")

person.name = "Tom"

print(person.name)
print(person.surname)
print(person)