import configparser


def calculate(value: int):
    # Putting the config parser in the function allows for changes in the config without
    # having to reload the program
    config = configparser.ConfigParser()
    config.read("./config.ini")
    # 2048 = 0C
    # 3000 = 23C
    # By dividing 3000-2048 / 23. You get 41.39 for each Celsius change
    # 41.39 = 1C change
    # 41.39130434782609
    celsius = round(float(value-2048) / 41.39, 2)
    fahrenheit = round((celsius * 1.8) + 32, 2)
    kelvin = round(273.15 + celsius, 2)
    # print(f"{math} Celsius")
    # print(f"\n{fahrenheit} Fahrenheit")
    # print(f"{kelvin} Kelvin")
    # print(f"{math} = {val1, val2}")
    if config["Sensor"]["Temperature"] == "Fahrenheit":
        math = fahrenheit
    elif config["Sensor"]["Temperature"] == "Kelvin":
        math = kelvin
    else:
        math = celsius
    return math
