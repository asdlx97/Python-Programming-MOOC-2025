"""
Please write a program which asks for the names and ages of two persons. 
The program should then print out the name of the elder.

Some examples of expected behaviour:

Sample output
Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada

Sample output
Person 1:
Name: Bill
Age: 1
Person 2:
Name: Jean
Age: 1
Bill and Jean are the same age

"""
# Write your solution here
print("Person 1:")
first_person_name = input("Name: ")
first_person_age = int(input("Age: "))

print("Person 2:")
second_person_name = input("Name: ")
second_person_age = int(input("Age: "))

if first_person_age > second_person_age:
    print(f"The elder is {first_person_name}")
elif first_person_age < second_person_age:
    print(f"The elder is {second_person_name}")
else:
    print(f"{first_person_name} and {second_person_name} are the same age")

"""
# Suggested solution
print("Person 1:")
name1 = input("Name: ")
age1 = int(input("Age: "))
 
print("Person 2:")
name2 = input("Name: ")
age2 = int(input("Age: "))
 
if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")
 

#Review
My solution results in the same output. Scripts are same except for using inverted comparison operators
instead of switching variables with same operator.
"""