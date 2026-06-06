#Develop a simple data processing script that reads a string input from the user, converts it into a list of words, and then uses a dictionary to count the occurrence of each word.

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
print("Word Count:", result)