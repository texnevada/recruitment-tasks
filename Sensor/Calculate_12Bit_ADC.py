
def calculate(value):
    # 2048 = 0C
    # 3000 = 23C
    # By dividing 3000-2048 / 23. You get 41.39 for each Celsius change
    # 41.39 = 1C change
    # 41.39130434782609
    val1 = 0
    val2 = 0
    if int(value) >= 2048:
        val1 = value
        val2 = 2048
    # Changing this to else. Will come back later to add if and error correction
    else:
        val1 = 2048
        val2 = value
    math = round(float(val1-val2) / 41.39, 2)
    return math
