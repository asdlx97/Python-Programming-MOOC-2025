"""
Please write a function named invert(dictionary: dict),
which takes a dictionary as its argument. The dictionary should be inverted
in place so that values become keys and keys become values.

An example of its use:

s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)

Sample output
{"first": 1, "second": 2, "third": 3, "fourth": 4}
NB: the principles regarding lists covered here also hold for dictionaries
passed as arguments.

If you have trouble completing this exercise, the visualisation tool might
help you understand what your code is or isn't doing.
"""


# Write your solution here
def invert(dictionary: dict):
    # Create new empty dictionary to avoid reference to original
    dictionary_copy = {}

    # Populate new dictionary with switched original values
    for key, value in dictionary.items():
        dictionary_copy[value] = key
        # del dictionary[key] #Not possible as you cannot change dict while in for loop

    # Clear original dictionary
    dictionary.clear()

    # Repopulate original one with inversed key-value pairs from new dictionary
    for key, value in dictionary_copy.items():
        dictionary[key] = value


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)

"""
# Suggested solution

def invert(dictionary: dict):
	copy = {}
	for key in dictionary:
		copy[key] = dictionary[key]
	for key in copy:
		del dictionary[key]
	for key in copy:
		dictionary[copy[key]] = key

#Review
My solution works correctly and produces the same result. Structurally, it’s slightly 
cleaner than the suggested one since it avoids deleting keys from the original 
dictionary mid-process, which can be risky. Instead, it builds a separate inverted 
copy and then replaces the contents of the original dictionary in one clear step. 
The suggested version accomplishes the same thing but uses three loops and direct deletions, 
making it a bit less efficient and harder to follow. 

Overall, I think my version is a more streamlined and safer approach to in-place inversion.
"""
