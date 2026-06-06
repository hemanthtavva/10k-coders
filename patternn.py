rows = 5
for i in range (1, rows+1):
    res=""
    for j in range (1, rows+1):
        if j==1 or j == rows or j == (rows//2)+1:
            res += "* "
        else:
            res += "  "
        print(res)