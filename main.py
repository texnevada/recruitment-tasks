#
# This is just to get things set up.
#
import time
from datetime import datetime
import Sensor.Read_Temperature as Sensor
from Sensor.Calculate_12Bit_ADC import calculate
from Sensor.HTTP_REST import post
import random
import configparser
start = time.perf_counter()
config = configparser.ConfigParser()
config.read("./config.ini")


def temperature_details(seconds: int):
    timeout_start = time.time()
    temp_values = []
    # UTC time
    datetime_start = datetime.utcnow().isoformat()

    while time.time() < timeout_start + seconds:
        value = Sensor.raw_read()
        temp = calculate(value)
        temp_values.append(temp)
        print(f"{temp} {config['Sensor']['Temperature']}")
    temp_values.sort()
    print(temp_values)
    print(temp_values[0])
    print(temp_values[-1])
    average_temp = sum(temp_values) / len(temp_values)
    datetime_end = datetime.utcnow().isoformat()
    json = {
        "time": {
            "start": datetime_start,
            "end": datetime_end
        },
        "min": temp_values[0],
        "max": temp_values[-1],
        "average": round(average_temp, 2)
    }
    print(json)
    post(json)


def main():
    while random.randrange(30):
        value = Sensor.raw_read()
        temp = calculate(value)
        print(f"{temp} {config['Sensor']['Temperature']}")


if __name__ == "__main__":
    temperature_details(120)
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 6)} second(s)")
