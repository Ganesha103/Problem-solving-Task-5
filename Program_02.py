my_list = ['apple', 'banana', 'cherry', 1]

# Using lambda function to check if all elements are strings
result = all(map(lambda x: type(x) == str, my_list))

print(result)  # Output: False, because 1 is not a string
