"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately.
You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the
button for executing tests .

A class named Series

Please write a class named Series with the following functionality:

dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
print(dexter)
Sample output
Dexter (8 seasons)
genres: Crime, Drama, Mystery, Thriller
no ratings
The constructor should take the title, the number of seasons and a list of genres for the series as
its arguments.

Hint: whenever you need to produce a string from a list containing strings, with a separating character
of your choice in between the entries, you can use the join method as follows:

genre_list = ["Crime", "Drama", "Mystery", "Thriller"]
genre_string = ", ".join(genre_list)
print(genre_string)
Sample output
Crime, Drama, Mystery, Thriller
Adding reviews

Please implement the method rate(rating: int) which lets you add a rating between 0 and 5 to any
series object. You will also need to adjust the __str__ method so that in case there are ratings,
the method prints out the number of ratings added, and their average rounded to one decimal point.

dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)

Sample output
Dexter (8 seasons)
genres: Crime, Drama, Mystery, Thriller
5 ratings, average 3.4 points
Searching for series

Please implement these two functions which allow you to search through a list of series:
minimum_grade(rating: float, series_list: list) and includes_genre(genre: str, series_list: list).

Here is an example of how the new methods are used:

s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)

Sample output
a minimum rating of 4.5:
Dexter
genre Comedy:
South Park
Friends
The code above and the automatic tests for this exercise assume your class
contains an attribute title. If you used some other attribute name to refer
to the name of the series, please change it before submitting.
"""

# Write your solution here:
from statistics import mean


class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        if not self.ratings:
            mean_result = "no ratings"
        else:
            mean_result = (
                f"{len(self.ratings)} ratings, average {mean(self.ratings):.1f} points"
            )
        return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{mean_result}"

    def rate(self, rating: int):
        self.ratings.append(rating)


def minimum_grade(grade: float, series_list: list):
    sorted_series = []

    for series in series_list:
        if mean(series.ratings) > grade:
            sorted_series.append(series)

    return sorted_series


def includes_genre(genre: str, series_list: list):
    sorted_series = []

    for series in series_list:
        if genre in series.genres:
            sorted_series.append(series)

    return sorted_series


if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

"""
# Suggested solution

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = [0, 0, 0, 0, 0, 0]
        self.number_of_ratings = 0
 
    def grade(self):
        if self.number_of_ratings == 0:
            return 0
        else:
            grade_sum = 0
            for i in range(0, 6):
                grade_sum += self.ratings[i] * i
            return grade_sum / self.number_of_ratings
 
 
    def __str__(self):
        genres = ", ".join(self.genres)
 
        if self.number_of_ratings == 0:
            ratings = "no ratings"
        else:
            grade_sum = 0
            for i in range(0, 6):
                grade_sum += self.ratings[i] * i
            ka = grade_sum / self.number_of_ratings
            ratings = f"{self.number_of_ratings} ratings, average {ka:.1f} points"
 
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genres}\n{ratings}"
 
    def rate(self, grade: int):
        self.number_of_ratings += 1
        self.ratings[grade] += 1
 
def minimum_grade(grade: float, seriest: list):
    result = []
    for series in seriest:
        if series.grade() >= grade:
            result.append(series)
 
    return result
 
def includes_genre(genre: str, seriest: list):
    result = []
    for series in seriest:
        if genre in series.genres:
            result.append(series)
 
    return result
 
if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    seriest = [s1, s2, s3]
 
    answer = minimum_grade(4.5, seriest)
    print(answer)


#Review
My solution results in the same output, suggested one increments
seconds first, and then checks for rollover to reset if necessary which
makes the code a bit more compact. 
"""
