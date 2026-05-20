"""Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.

my_list = ["first", "second", "fourth", "eleventh"]

result = shortest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = shortest(my_list)
print(result)
Sample output
first
tim"""

# Write your solution here
def shortest(my_list: list):
    shortest = my_list[0]

    for word in my_list:
        if len(word) <= len(shortest):
            shortest = word

    return shortest #Compared to previous exercise, here we return name itself, not the length of it

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)

"""
# Suggested Solution

def shortest(names: list):
    result = ""
 
    for nimi in names:
        if result == "" or len(nimi) < len(result):
            result = nimi
 
    return result

#Review
My solution resulted in the same output, The suggested one did however also check 
for empty strings in the list, but the assignment said we could assume there wouldn't be any.

"""