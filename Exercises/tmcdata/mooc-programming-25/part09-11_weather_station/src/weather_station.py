"""
Please create a class named WeatherStation which is used to store observations about the weather. The class should have the following public attributes:

a constructor which takes the name of the station as its argument
a method named add_observation(observation: str) which adds an observation as the last entry in a list
a method named latest_observation() which returns the latest observation added to the list. If there are no observations yet, the method should return an empty string.
a method named number_of_observations() which returns the total number of observations added
a __str__ method which returns the name of the station and the total number of observations added as per the example below.
All attributes should be encapsulated, so they can't be directly accessed. It is up to you how you implement the class, as long as the public interface is exactly as described above.

An example of how the class is used:

station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)

Sample output
Sunny
Thunderstorm
3
Houston, 3 observations
"""


# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observations = []

    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

    def add_observation(self, description: str):
        self.__observations.append(description)

    def latest_observation(self):
        if not self.__observations:
            return ""
        else:
            return self.__observations[-1]

    def number_of_observations(self):
        return len(self.__observations)


if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

"""
# Suggested solution

class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observations = 0
        self.__latest_observation = ""
 
    def add_observation(self, observation: str):
        self.__latest_observation = observation
        self.__observations += 1
 
    def latest_observation(self):
        return self.__latest_observation
 
    def number_of_observations(self):
        return self.__observations 
 
    def __str__(self):
        return f"{self.__name}, {self.__observations} observations"

#Review
My solution results in the same output, suggested one uses
an extra instance trait to store the latest added observation
within the add_observation() method, rather than returning the last
object from the observations list in my solution.
"""
