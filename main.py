#
# This is just to get things set up.
#
import Sensor.Read_Temperature as Sensor


def main():
    value = Sensor.read()
    print(value)


if __name__ == "__main__":
    main()
