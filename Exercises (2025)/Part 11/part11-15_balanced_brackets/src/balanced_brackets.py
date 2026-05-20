
"""
The exercise template contains the function balanced_brackets which takes a string as its argument. It checks if the round brackets, or parentheses, within the string are balanced. That is, for each opening bracket ( there should be a closing bracket ), and all pairs of brackets should be matched in order, i.e. the bracket pairs must not be crossed.

def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])

ok = balanced_brackets("(((())))")
print(ok)

# there is one closing bracket too many, so this produces False
ok = balanced_brackets("()())")
print(ok)

# this one starts with a closing bracket, False again
ok = balanced_brackets(")()")
print(ok)

# this produces False because the function only handles entirely nested brackets
ok = balanced_brackets("()(())")
print(ok)
Sample output
True
False
False
False
Please expand the function so that it also works with square brackets []. The function should also ignore all characters which are not brackets () or []. The different types of brackets must be matched correctly in order.

Please have a look at the examples below::

ok = balanced_brackets("([([])])")
print(ok)

ok = balanced_brackets("(python version [3.7]) please use this one!")
print(ok)

# this is no good, the closing bracket doesn't match
ok = balanced_brackets("(()]")
print(ok)

# different types of brackets are mismatched
ok = balanced_brackets("([bad egg)]")
print(ok)
NB: the function only needs to handle entirely nested brackets. The string (x + 1)(y + 1) should produce False as the brackets are not nested within each other.

Sample output
True
True
False
False
"""

def balanced_brackets(my_string: str):
    #Filtering out non brackets by using list comprehension with a string as basis like we saw in part 11.2
    my_string = "".join([character for character in my_string if character in ["(",")","[","]"]])
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)

"""
#Suggested solution

def balanced_brackets(mj: str):
    # string is empty, so it is ok
    if len(mj) == 0:
        return True
 
    # if first character is not any bracket, let's eat it away
    if not mj[0] in "()[]":
        return balanced_brackets(mj[1:])
 
    # if last is not any bracket, let's eat it away
    if not mj[-1] in "()[]":
        return balanced_brackets(mj[:-1])
    
    # now is known that first and last characters are brackets
    # check if they are a pair
    if mj[0]=="(" and mj[-1]==")":
        return balanced_brackets(mj[1:-1])
    if mj[0]=="[" and mj[-1]=="]":
        return balanced_brackets(mj[1:-1])
 
    # were not, so this string is not ok
    return False
 
 
    # remove first and last character
 
#Review
My solution results in the same output, the suggested one is exactly the same.
"""