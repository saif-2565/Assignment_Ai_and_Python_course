# Fibonacci Sequence
terms = int(input("Enter number of terms: "))

# Starting two numbers
first = 0
second = 1

if terms <= 0: # to check term is positive or not 
    print("Please enter a positive number of terms.")
elif terms == 1:
    print(first)
else:
    print(first, second, end=" ")
    for i in range(2, terms):
        next_num = first + second
        print(next_num, end=" ")
        first = second
        second = next_num
