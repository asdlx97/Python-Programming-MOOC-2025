"""
Fix the syntax
Points:
0
/
1
The following program contains several syntactic errors. 
Please fix the program so that the syntax is in order and the program works as specified by the examples below.

Sample output
Please type in a number: 13
13 must be my lucky number!
Have a nice day!

Sample output
Please type in a number: 101
The number was greater than one hundred
Now its value has decreased by one hundred
Its value is now 1
1 must be my lucky number!
Have a nice day!

# Fix the program
  number = input("Please type in a number: ")
  if number>100
    print("The number was greater than one hundred")
    number - 100
    print("Now its value has decreased by one hundred)
      print("Its value is now"+ number)
 print(number + " must be my lucky number!")
 print("Have a nice day!)
"""
# Fix the program
number = int(input("Please type in a number: ")) #Was indented, missing conversion to int type

if number > 100: #Was indented, missing colon
    print("The number was greater than one hundred")#Was indented
    number -= 100 #Was indented, missing equal sign in operator
    print("Now its value has decreased by one hundred") #Was indented, missing closing double brackets
    print("Its value is now", number)#Was indented, and int type had to be converted to str() OR use comma separated printing, went for the latter

print(str(number) + " must be my lucky number!")#Number variable had to be converted to str() OR use f-string
print("Have a nice day!")#Missing closing double brackets

"""
#Suggested Solution

number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number = number - 100
    print("Now its value has decreased by one hundred")
    print("Its value is now"+ str(number))
print(str(number) + " must be my lucky number!")
print("Have a nice day!")

#Review
My solution results in the same output, the suggested one uses more elaborate airithemic where mine is more concise.
F-strings are more reasable than str() conversions and comma joins, si I'd prefer using those in the future but
was good practise to use other methods here.
"""