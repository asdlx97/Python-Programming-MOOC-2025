# Write your solution to exercise 1 here
string_count = 0
longest_string_length = 0
character_freq = {}
most_common_character = ""
max_character_freq = 0

while True:
    string = input("Type in a string: ")

    if string == "":
        break

    # I guess i could also collect strings in a list count the items after breaking this while loop but this is my first go to
    string_count += 1

    # Same here, I could collect strings in a list and loop through it after breaking this while loop but this works
    if len(string) > longest_string_length:
        longest_string_length = len(string)

    # At first I wanted to populate a dict with every character in string.ascii_lowercase as key and 0 as value, to then increase on encounter, but seems like this isn't necessary, I'll populate on encountering
    for character in string:
        if character not in character_freq:
            character_freq[character] = 0
        character_freq[character] += 1

for character in character_freq:
    if character_freq[character] > max_character_freq:
        max_character_freq = character_freq[character]
        most_common_character = character

print(f"Total number of strings: {string_count}")
print(f"The length of the longest string: {longest_string_length}")
print(f"The most common character in strings: {most_common_character}")
