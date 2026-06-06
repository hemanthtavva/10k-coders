#Write a function that takes a list of integers as input, calculates the mean, median, and standard deviation, and returns these values as a dictionary.

def cal(num):
    mean = sum(num) / len(num)
    median = sorted(num)[len(num) // 2] if len(num) % 2 != 0 else (sorted(num)[len(num) // 2 - 1] + sorted(num)[len(num) // 2]) / 2
    std_dev = (sum((x - mean) ** 2 for x in num) / len(num)) ** 0.5
    return {"mean": mean, "median": median, "std_dev": std_dev}
num = list(map(int, input().split()))
print(cal(num))
