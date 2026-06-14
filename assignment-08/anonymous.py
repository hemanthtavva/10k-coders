#1. Define a lambda function to square each number in a given list of integers.

nums = [1, 2, 3, 4, 5]
square =lambda x: x**2
def square_list(nums):
    for i in nums:
        print(square(i))

square_list(nums)
   


#2. Use the map() function along with a lambda function to convert all strings in a list to uppercase.
listt = ['hello', 'world', 'python']
upper_list = list(map(lambda x: x.upper(), listt))
print(upper_list)



#3. Utilize the filter() function with a lambda function to extract only the even numbers from a list of integers.
nums = [1,2,3,4,5,6,7,8]
even_nums = list(filter(lambda x: x%2==0,nums))
print(even_nums)



#4. Apply the reduce() function from the functools module, combined with a lambda function, to calculate the sum of all numbers in a list.
from functools import reduce
nums = [1,2,3,4,5,6,7]
res = reduce (lambda x,y : x + y, nums, 0)
print(res)



#5. Implement a function that takes a list of dictionaries as input, where each dictionary represents a person with 'name' and 'age' keys, and uses anonymous functions to extract the names of all individuals older than 30.
people = [{'name': 'Hemanth', 'age': 22},
           {'name': 'dinesh', 'age': 25}, 
           {'name': 'murthy', 'age': 56}, 
           {'name': 'pushpa', 'age': 50}]
def extract_names(people):
    older_than_30 = list(filter(lambda x: x['age'] > 30, people))
    names = list(map(lambda x:x['name'], older_than_30))
    print(names)

extract_names(people)