# Tables
# Check whether entered number is positive or not, loop keep asking till positive number entered 
while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        break
    else:
        print("Please enter a positive number!")

# Print table from 1 to 10
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
