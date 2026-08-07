rows = 5
for i in range (1, rows+1):
    res=""
    for j in range (1, rows+1):
        if j==1 or j == rows or j == (rows//2)+1:
            res += "* "
        else:
            res += "  "
        print(res)

# even if we want to uodate a dupilicate value it will not add same extra value
nums = {1,2,3,4,5}
nums.add(3)
print(nums)
nums.add(6)
print(nums)
