# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self._name = name
        self._grade = grade
        self._credits = credits

    def __str__(self):
        return f"{self._name} ({self._credits} cr) grade {self._grade}"


class CourseRecords:
    def __init__(self):
        self.courses = {}

    def add_course(self, name, grade, credits):
        # Same records can overwrite only if grade higher, can never be lower
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
        grade_distribution = {"5": "", "4": "", "3": "", "2": "", "1": ""}
        for course in self.__courserecords.courses.values():
            total_grades += course._grade
            total_credits += course._credits
            total_courses += 1
            for grade in grade_distribution:
                if grade == str(course._grade):
                    grade_distribution[grade] += "x"
        mean = total_grades / total_courses
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
