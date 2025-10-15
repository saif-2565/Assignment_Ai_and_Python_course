# Find Maximum and Minimum Program (Without using max or min functions)

# Take input and convert to integer list
numbers = input("Enter numbers separated by spaces:\n")
# Using spaces easily and correctly track the user entered numbers 
num_list = [int(x) for x in numbers.split()]

# Assume first element as max and min
maximum = num_list[0]
minimum = num_list[0]

# Loop through the list to find max and min
for n in num_list:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

# Print the results
print("Maximum number:", maximum)
print("Minimum number:", minimum)
