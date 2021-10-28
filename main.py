#
# This is just to get things set up.
#
import time
import Sensor.Read_Temperature as Sensor
from Sensor.Calculate_12Bit_ADC import calculate
import random
import configparser
start = time.perf_counter()


def main():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    while random.randrange(30):
        value = Sensor.read()
        temp = calculate(value)
        print(f"{temp} {config['Sensor']['Temperature']}")


if __name__ == "__main__":
    main()
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 6)} second(s)")
