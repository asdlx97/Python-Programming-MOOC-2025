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
