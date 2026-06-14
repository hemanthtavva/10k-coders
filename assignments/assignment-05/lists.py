#1. Implement a Python function remove_duplicates that takes a list as input, removes duplicate elements, and returns the resulting list.
def rem_dup(lst):
    seen = []
    for i in lst:
        if i not in seen:
            seen.append(i)
    return seen

print(rem_dup([1, 2, 3, 2, 4, 1, 5])) 

lst = list(map(int, input().split()))
result = rem_dup(lst)
print(result)




#2. Write a function find_max that finds the maximum value in a list of integers and returns its index.
def find_max(lst):
    max_index = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[max_index]:
            max_index = i
    return max_index

print(find_max([1,3,5,6,77,4,5]))




#3. Create a function filter_even that filters out odd numbers from a given list and returns a new list containing only the even numbers.
def filter_even(lst):
    even_num=[]
    for i in lst:
        if i % 2 ==0:
            even_num.append(i)
    return even_num

print(filter_even([1,2,3,4,5,6,7,8,9,10]))




#4. Develop a function sum_elements that calculates the sum of all elements in a list of numbers.
def sum_elements(lst):
    total =0
    for i in lst:
        total = total + i
    return total

print(sum_elements([1,2,3,4,5,6,7,8,9]))





#5. Use list comprehension to create a new list double_values that contains double the values of the original list.
def double_values(lst):
    double=[]
    for i in lst:
        double.append(i*2)
    return double

print(double_values([1,2,4,5,6]))
        