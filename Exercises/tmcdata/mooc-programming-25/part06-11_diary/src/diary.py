"""
Please write a program which works as a simply diary. The diary entries should be saved
in the file diary.txt. When the program is executed, it should first read any entries
already in the file.

NB: the automatic tests for this exercise will change the contents of the file.
If you want to keep its contents, first make a copy of the file under a different name.

The program should work as follows:

Sample output
1 - add an entry, 2 - read entries, 0 - quit
Function: 1
Diary entry: Today I ate porridge
Diary saved

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
1 - add an entry, 2 - read entries, 0 - quit
Function: 1
Diary entry: I went to the sauna in the evening
Diary saved

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
I went to the sauna in the evening
1 - add an entry, 2 - read entries, 0 - quit
Function: 0
Bye now!
When the program is executed for the second time, this should happen:

Sample output
1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
I went to the sauna in the evening
1 - add an entry, 2 - read entries, 0 - quit
Function: 0
Bye now!
NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    commando = int(input("Function: "))

    if commando == 0:
        print("Bye now!")
        break
    elif commando == 2:
        print("Entries: ")
        with open("diary.txt") as new_file:
            print(new_file.read())
    elif commando == 1:
        diary_entry = input("Diary entry: ")
        with open("diary.txt", "a") as new_file:
            new_file.write(f"{diary_entry}\n")
        print("Diary saved")

"""
# Suggested solution

# Read the markings first
with open("diary.txt") as file:
    content = []
    for row in file:
        content.append(row.replace("\n",""))
 
# Open file for appending
with open("diary.txt", "a") as file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = input("Function: ")
        if function == "1":
            entry = input("Diary entry: ")
            file.write(entry + "\n")
            content.append(entry)
            print("Diary saved")
        elif function == "2":
            print("Entries:")
            for entry in content:
                print(entry)
        elif function == "0":
            print("Bye now!")
            break

#Review
The suggested solution keeps a list of entries in memory (content) so it doesn’t 
reopen the file for reading each time. That makes it slightly more efficient for 
repeated “read” operations. My version reopens the file on every read, which is 
simpler and still perfectly valid for this small-scale task.
 """
