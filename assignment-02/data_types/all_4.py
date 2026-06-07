#1.Create a Python program that declares and initializes variables of different datatypes (integer, float, string, list, dictionary) and prints their types using the type() function.

a = 10
b = 3.14
c = "Hello, World!"
d = [1, 2, 3, 4, 5]
e = {"name": "Hemanth", "age": 21, "city": "Hyderabad"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))




#2. Write a function that takes a list of integers as input, calculates the mean, median, and standard deviation, and returns these values as a dictionary.

def cal(num):
    mean = sum(num) / len(num)
    median = 0
    sorted_num = sorted(num)
    n = len(num)
    if n % 2 == 1:
        median = sorted_num[n // 2]
    else:
        median = (sorted_num[n // 2 - 1] + sorted_num[n // 2]) / 2
        
    std_dev = (sum((x - mean) ** 2 for x in num) / len(num)) ** 0.5
    return {"mean": mean, "median": median, "std_dev": std_dev}
num = list(map(int, input().split()))
print(cal(num))





#3. Develop a simple data processing script that reads a string input from the user, converts it into a list of words, and then uses a dictionary to count the occurrence of each word.

def count_words(input_string):
    words = input_string.split()
    word_count= {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
input_string = input("Enter a string: ")
result = count_words(input_string)
print(result)





#4. Implement a class that represents a person with attributes like name (string), age (integer), and address (dictionary). Create instances of this class and demonstrate how to access and modify their attributes.

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