'''Reads the temperature of the cpu from linux'''


def read_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as file:
        raw_temperature = file.read()

    # Represent temperature in degrees C
    temperature = float(raw_temperature) / 1000.0

    return temperature