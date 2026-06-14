#1.Create a Python script that initializes a list of integers from 1 to 20.
nums= list(range(1,21))
print(nums)




#2.Use list methods to append, insert, and remove elements from the list.
#append
nums.append(21)
print(nums)

#insert
nums.insert(21,22)
print(nums)

#remove
nums.remove(22)
print(nums)




#3.Implement a function to sort the list in ascending and descending order using list methods.
nums = [5, 2, 9, 1, 5, 6]
def sort_list(nums):
    asc= sorted(nums)
    print(asc)
    desc= sorted(nums, reverse=True)
    print(desc)
sort_list(nums)



#4.Use list comprehension to generate a new list containing the squares of numbers from the original list.
nums = [1,2,3,4,5]
def square_list(nums):
    square_list = [i**2 for i in nums]
    print(square_list)
square_list(nums)