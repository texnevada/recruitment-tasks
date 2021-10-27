# Since there is no "real" temperature sensor. It makes sense to read values from random lines of the txt file
import random
import time


def read():
    # 100ms delay before read
    time.sleep(0.1)
    # Reads the temperature values
    with open("./temperature-sensor/temperature.txt") as sensor:
        # Loops until random hits 8 to simulate a temperature reader.
        for value in sensor:
            if random.randrange(10) == 8:
                # Returns the value as a integer instead of string
                return int(value)
