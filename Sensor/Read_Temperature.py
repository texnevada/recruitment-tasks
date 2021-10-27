# Since there is no "real" temperature sensor. It makes sense to read values from random lines of the txt file
import random


def read():
    with open("./temperature-sensor/temperature.txt") as sensor:
        for value in sensor:
            if random.randrange(10) == 8:
                return value
