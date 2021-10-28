# Since there is no "real" temperature sensor. It makes sense to read values from random lines of the txt file
import random
import time
import configparser


def raw_read():
    # Putting the config parser in the function allows for changes in the config without
    # having to reload the program
    config = configparser.ConfigParser()
    config.read("./config.ini")
    time.sleep(float(config["Sensor"]["sensor_read_speed"]))
    # Reads the temperature values
    with open("./temperature-sensor/temperature.txt") as sensor:
        # Loops until random hits 8 to simulate a temperature reader.
        for value in sensor:
            if random.randrange(10) == 8:
                # Returns the value as a integer instead of string
                return int(value)
