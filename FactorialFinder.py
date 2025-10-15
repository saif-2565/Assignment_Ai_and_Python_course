# Factorial Finder Program

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial only exists of positive number")
else:
    factorial = 1
# Loop to find Factorial 
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Factorial of", num, " = ", factorial)
