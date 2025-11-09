

# Write your solution here
def first_word(string):
    length = len(string)
    index = 0

    while index < length:
        if string[index] == " ":
            return string[0:index]
            break
        index += 1

def second_word(string):
    length = len(string)
    start_index = len(first_word(string)) + 1
    index = start_index

    while index < length:
        if string[index] == " ":
            return string[start_index:index]
            break
        index += 1
    
    return string[start_index:length]


def last_word(string):
    length = -len(string)
    index = -1

    while index > length:
        if string[index] == " ":
            return f"{string[index+1:-1]}{string[-1]}"
            break
        index -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "sumin gaat"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

