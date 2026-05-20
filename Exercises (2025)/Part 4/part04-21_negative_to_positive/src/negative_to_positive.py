"""
Please write a program which asks the user for a positive integer N. 
The program then prints out all numbers between -N and N inclusive, 
but leaves out the number 0. Each number should be printed on a separate line.

An example of expected behaviour:

Sample output
Please type in a positive integer: 4
-4
-3
-2
-1
1
2
3
4

NB: this exercise doesn't ask you to write any functions, 
so you should not place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
n = int(input("Please type in a positive integer: "))

for i in range(-n, n+1):
    if i!=0:
        print(i)

"""
# Suggested Solution

number = int(input("Please type in a positive integer: "))
 
for i in range(-number, number + 1):
    # Because in Python bool-type equals to
    # 0 and 1 (False and True), condition can also be written as follows
    # if i:
    if i != 0:
        print(i)

#Review
Same script, same output. 
"""