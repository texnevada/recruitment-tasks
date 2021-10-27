#
# This is just to get things set up.
#
import Sensor.Read_Temperature as Sensor
from Sensor.Calculate_12Bit_ADC import calculate


def main():
    value = Sensor.read()
    temp = calculate(value)
    print(temp)


if __name__ == "__main__":
    main()
