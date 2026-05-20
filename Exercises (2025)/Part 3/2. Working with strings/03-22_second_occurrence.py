"""
Please write a program which finds the second occurrence of a substring. 
If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. 

For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:

Sample output
Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output
Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output
Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string.

"""
# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

if substring in string:
    first_index = string.find(substring) #Finding index of first occurence
    sliced_string = string[first_index+len(substring):] #Slice the rest of string after first occurence
    if substring in sliced_string: #Check if substring also occurs in sliced string
        sliced_index = string[first_index+len(substring):].find(substring) #Finding index of occurence in sliced string
        second_index = first_index + sliced_index + len(substring) #Calculate index of second occurence in whole string by adding both indexes plus length of substring to overlap inbetweens
        print(f"The second occurrence of the substring is at index {second_index}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")

"""
# Suggested solution

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
 
index1 = string.find(substring)
index2 = -1
if index1 != -1:
    string = string[index1+len(substring):]
    index2 = string.find(substring)
 
if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print("The second occurrence of the substring is at index " + str(index1+len(substring)+index2) +  ".")

#Review
My solution results in the same output, suggested first checks if .find() method results in a not found or '-1' meaning there is no index.
While I first check if substring occurs in string. Suggested skips that and also sets up a second index already before knowing first one exists, assuming second one
doesn't exist by giving it -1 value. Suggested one also reassigns sliced string to original string variable which is ok but I rather keep original one too just in case.

#TODO Rewrite finding second index using .find() method with two parameters so you don't have to calc index of sliced string?
""" 



