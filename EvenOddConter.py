# Even and Odd Counter Program

# Take input and convert to integer list
numbers = input("Enter numbers separated by spaces:\n")
# Using spaces easily and correctly track the user entered numbers 
numbers_list = [int(x) for x in numbers.split()]

even_count = 0
odd_count = 0

# Check each number
for num in numbers_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
