"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

Please write an interactive application for keeping track of your studies. The internal structure is up to you, but this would be a good opportunity to practice creating a similar structure as in the PhoneBook example above.

Your program should work as follows:

Sample output
1 add course
2 get course data
3 statistics
0 exit

command: 1
course: ItP
grade: 3
credits: 5

command: 2
course: ItP
ItP (5 cr) grade 3

command: 1
course: ItP
grade: 5
credits: 5

command: 2
course: ItP
ItP (5 cr) grade 5

command: 1
course: ItP
grade: 1
credits: 5

command: 2
course: ItP
ItP (5 cr) grade 5

command: 2
course: Introduction to Java
no entry for this course

command: 1
course: ACiP
grade: 1
credits: 10

command: 1
course: ItAI
grade: 2
credits: 5

command: 1
course: Algo101
grade: 4
credits: 1

command: 1
course: CompModels
grade: 5
credits: 8

command: 3
5 completed courses, a total of 29 credits
mean 3.4
grade distribution
5: xx
4: x
3:
2: x
1: x

command: 0
Each course name should result in a single entry in the records. A grade may be raised by re-entering the course details, but the grade should never be lowered.

This exercise is worth two exercise points. The first is granted after the commands 1, 2 and 0 work correctly in your program. The second is granted if command 3 also works as expected.
"""

# tee ratkaisusi tänne
class Course:
    def __init__(self, name:str, grade:int, credits:int):
        self._name = name
        self._grade = grade
        self._credits = credits

    def __str__(self):
        return f"{self._name} ({self._credits} cr) grade {self._grade}"


class CourseRecords:
    def __init__(self):
        self.courses = {}

    def add_course(self, name, grade, credits):
        #Same records can overwrite only if grade higher, can never be lower
        if name in self.courses and self.courses[name]._grade > grade:
            pass
        else:
            self.courses[name] = Course(name, grade, credits)

    def get_course_data(self, name):
        if name in self.courses:
            return self.courses[name]
        else:
            return None


class CourseRecordsApplication:
    def __init__(self):
        self.__courserecords = CourseRecords() 

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))

        self.__courserecords.add_course(name, grade, credits)
        
    def get_course_data(self):
        name = input("course: ")
        data = self.__courserecords.get_course_data(name)
        if data == None:
            print("no entry for this course")
        else:
            print(data)

    def statistics(self):
        total_courses = 0
        total_grades = 0
        total_credits = 0
        grade_distribution = {
            "5":"", "4":"", "3":"", "2":"", "1":""
        }
        for course in self.__courserecords.courses.values():
            total_grades += course._grade
            total_credits += course._credits
            total_courses += 1
            for grade in grade_distribution:
                if grade == str(course._grade):
                    grade_distribution[grade] += "x"
        mean = total_grades/total_courses
        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {round(mean, 1)}")
        print("grade distribution")
        for key, value in grade_distribution.items():
            print(f"{key}: {value}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()


application = CourseRecordsApplication()
application.execute()

"""
#Suggested Solution 

class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name 
        self.__grade = grade
        self.__credits = credits
 
    def grade(self):
        return self.__grade
 
    def credits(self):
        return self.__credits
 
    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
 
class StudyRecords:
    def __init__(self):
       self.courses = {}    
 
    def add_completion(self, course_name, grade, op):
        if course_name in self.courses and self.courses[course_name].grade() > grade:
            return
 
        self.courses[course_name] = Course(course_name, grade, op)
 
    def get_completion(self, course_name):
        if not course_name in self.courses:
            return None
 
        return self.courses[course_name]        
 
    def get_statistics(self):
        number_of_courses = len(self.courses)
        credits = 0
        sum_of_grades = 0
        grades = [0, 0, 0, 0, 0, 0, 0]
 
        for courses in self.courses.values():
            credits += courses.credits()
            sum_of_grades += courses.grade()
            grades[courses.grade()] += 1
        
        return {
            "number_of_courses": number_of_courses,
            "credits": credits,
            "average": sum_of_grades / number_of_courses,
            "grades": grades
        }
 
class Application:
    def __init__(self):
        self.register = StudyRecords()     
 
    def ohje(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
 
    def new_completion(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        op = int(input("credits: "))
        self.register.add_completion(course_name, grade, op)
 
    def get_completion(self):
        course_name = input("course: ")
        courses = self.register.get_completion(course_name)
        if courses is None:
            print("no entry for this course")
        else:
            print(courses)        
 
    def statistics(self):
        t = self.register.get_statistics() 
 
        print(f"{t['number_of_courses']} completed courses, a total of {t['credits']} credits")
        print(f"mean {t['average']:.1f}")
        print("grade distribution")
        for i in range(5, 0, -1):
            grade_hits = t['grades'][i]
            row = "x"*grade_hits
            print(f"{i}: {row}")        
 
    def execute(self):
        self.ohje()
 
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command=="1":
                self.new_completion()
            elif command=="2":
                self.get_completion()
            elif command=="3":
                self.statistics()
 
Application().execute()

#Review
My solution produces the same output, the main difference
with the suggested solution is that my statistics calculations
are done within the Application class rather than under the 
CourseRecords class as the suggested one does, the latter surely 
makes more sense as the application should just print out returned
results like the other methods within the Application class. 
"""