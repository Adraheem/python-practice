def temperature_conversion(temp, target):
    temperature = 0
    if target == "K":
        temperature = temp + 273.15
    elif target == "C":
        temperature = temp - 273.15
    print(temperature)

    return temperature
