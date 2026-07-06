import os
# print(os.getcwd())
#change directory
#cd.. is one way to go back to the previous directory
print(os.getcwd(), "before changing directory")
os.chdir("/Users/hemanthtavva/Desktop/10k_coders/python/os")
print(os.getcwd(), "after changing directory")
