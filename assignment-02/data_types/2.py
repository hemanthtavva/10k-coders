#Write a function that takes a list of integers as input, calculates the mean, median, and standard deviation, and returns these values as a dictionary.

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
