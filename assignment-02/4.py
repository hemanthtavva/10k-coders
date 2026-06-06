#Implement a class that represents a person with attributes like name (string), age (integer), and address (dictionary). Create instances of this class and demonstrate how to access and modify their attributes.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


person1 = Person("Hemanth", 21, {"city": "Hyderabad", "country": "India"})
print("Name:", person1.name)
print("Age:", person1.age)
print("Address:", person1.address) 

# Modifying attributes
person1.name = "Hemanth Tavva"
person1.age = 22
person1.address["city"] = "vijayawada"
print("Name:", person1.name)
print("Age:", person1.age)
print("Address:", person1.address)