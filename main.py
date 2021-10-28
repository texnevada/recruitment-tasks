#
# This is just to get things set up.
#
import time
import Sensor.Read_Temperature as Sensor
from Sensor.Calculate_12Bit_ADC import calculate
import random
import configparser
start = time.perf_counter()
config = configparser.ConfigParser()
config.read("./config.ini")


def temperature_details(seconds: int):
    timeout_start = time.time()
    temp_values = []
    while time.time() < timeout_start + seconds:
        value = Sensor.raw_read()
        temp = calculate(value)
        temp_values.append(temp)
        print(f"{temp} {config['Sensor']['Temperature']}")
    temp_values.sort()
    print(temp_values)


def main():
    while random.randrange(30):
        value = Sensor.raw_read()
        temp = calculate(value)
        print(f"{temp} {config['Sensor']['Temperature']}")


if __name__ == "__main__":
    temperature_details(5)
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 6)} second(s)")
