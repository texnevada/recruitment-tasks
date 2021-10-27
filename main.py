#
# This is just to get things set up.
#
import time
import Sensor.Read_Temperature as Sensor
from Sensor.Calculate_12Bit_ADC import calculate
start = time.perf_counter()


def main():
    value = Sensor.read()
    temp = calculate(value)
    print(temp)


if __name__ == "__main__":
    main()
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 6)} second(s)")
