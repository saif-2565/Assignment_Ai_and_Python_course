# Dictionary Keys and Values Program 

# Create empty dictionary
people = {}

# Ask for number of entries user want to add
num_entries = int(input("How many people do you want to add? "))

# Take inputs 
for i in range(num_entries):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    people[name] = age

# Make lists of keys and values
keys_list = list(people.keys())
values_list = list(people.values())

# Print dictionary, keys and values
print("\nYour Dictionary:", people)
print("Keys:", keys_list)
print("Values:", values_list)
