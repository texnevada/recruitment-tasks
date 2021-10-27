#
# This is just to get things set up.
#
import time
import Sensor.Read_Temperature as Sensor
from Sensor.Calculate_12Bit_ADC import calculate
import random
start = time.perf_counter()


def main():
    while random.randrange(30):
        value = Sensor.read()
        temp = calculate(value)
        print(f"{temp} Celsius")


if __name__ == "__main__":
    main()
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 6)} second(s)")
