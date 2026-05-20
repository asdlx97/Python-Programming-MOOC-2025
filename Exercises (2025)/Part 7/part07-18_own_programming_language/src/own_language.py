import string


# Write your solution here
def run(program):
    result = []
    variables = {}

    # Pre-populate our variables as they should start as 0
    for variable in string.ascii_uppercase:
        variables[variable] = 0

    for row in program:
        row = row.split(" ")

        if row[0] == "PRINT":
            try:
                result.append(int(row[1]))
            except ValueError:
                result.append(variables[row[1]])
        elif row[0] == "MOV":
            if row[2] in string.ascii_uppercase:
                variables[row[1]] = int(variables[row[2]])
            else:
                variables[row[1]] = int(row[2])
        elif row[0] == "ADD":
            if row[2] in string.ascii_uppercase:
                variables[row[1]] += int(variables[row[2]])
            else:
                variables[row[1]] += int(row[2])
        elif row[0] == "SUB":
            if row[2] in string.ascii_uppercase:
                variables[row[1]] -= int(variables[row[2]])
            else:
                variables[row[1]] -= int(row[2])
        elif row[0] == "MUL":
            if row[2] in string.ascii_uppercase:
                variables[row[1]] *= int(variables[row[2]])
            else:
                variables[row[1]] *= int(row[2])
        elif row[0] == "END":
            break

    return result


if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
