
def calculate(value):
    # 2048 = 0C
    # 3000 = 23C
    # 41.39 = 1C change
    if int(value) >= 2048:
        math = round(float((value-2048)/41.39130434782609), 2)
    elif int(value) < 2048:
        math = round(float((2048-value) / 41.39130434782609), 2)
    else:
        math = 0
    return math
