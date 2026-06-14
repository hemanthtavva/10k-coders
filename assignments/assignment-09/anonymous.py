#1.Define an anonymous function that takes a string as input and returns the string in uppercase.
nums = [1, 2, 3, 4, 5]
square =lambda x: x**2
def square_list(nums):
    for i in nums:
        print(square(i))

square_list(nums)




#2.Use the map() function along with an anonymous function to square all numbers in a given list.
listt = ['hello', 'world', 'python']
upper_list = list(map(lambda x: x.upper(), listt))
print(upper_list)





#3.Utilize the filter() function with an anonymous function to extract all even numbers from a list.
nums = [1,2,3,4,5,6,7,8]
even_nums = list(filter(lambda x: x%2==0,nums))
print(even_nums)




#4. Write a Python program that uses the reduce() function from the functools module along with an anonymous function to calculate the product of all elements in a list.
from functools import reduce
nums = [1,2,3,4,5,6,7]
res = reduce (lambda x,y : x * y, nums, 1)
print(res)





#5.Create a list of dictionaries representing people with their names and ages, then use anonymous functions with map(), filter(), and sorted() to perform the following operations:
# Extract all names from the list of people.
# Filter out people who are under 18 years old.
# Sort the list of people by age in descending order.
people = [{'name': 'Hemanth', 'age': 22},
           {'name': 'dinesh', 'age': 25}, 
           {'name': 'murthy', 'age': 56}, 
           {'name': 'pushpa', 'age': 50}]

#names
names = list(map(lambda x:x['name'], people))
print(names)

#filter 18 and above
adults = list(filter(lambda x:x['age'] >18, people))
print(adults)

#sort by age
sorted_people = list(sorted(people, key = lambda x:x['age'], reverse = True))
print(sorted_people)