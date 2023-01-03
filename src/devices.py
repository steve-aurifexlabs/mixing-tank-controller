'''Select and configure device drivers'''

def get_devices(config):
    devices = {}

    from drivers.linux.cpu_temp import read_cpu_temp
    devices['temperature_sensor'] = {
        'read': read_cpu_temp,
    }

    from drivers.periphery.button import Button
    devices['fan_button'] = {
        'read': Button(config["buttons"]["fan"]).read
    }
    # devices['alarm_reset_button'] = {
    #     'read': Button(config["buttons"]["alarm_reset"]).read
    # }

    from drivers.periphery.fan import Fan
    devices['fan'] = {
        'write': Fan(config["fan"]).write
    }

    from drivers.periphery.led import Led
    devices['warning_led'] = {
        'write': Led(config["leds"]["warning"]).write
    }
    # devices['alarm_led_0'] = {
    #     'write': Led(config["leds"]["alarm_0"]).write
    # }
    # devices['alarm_led_1'] = {
    #     'write': Led(config["leds"]["alarm_1"]).write
    # }

    return devices