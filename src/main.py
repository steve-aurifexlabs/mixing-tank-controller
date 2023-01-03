#!/usr/bin/env python


import asyncio
import sys
import json

import rtos.rtos as rtos
from rtos.timer import Timer
from devices import get_devices

from hal.sensor.temperature import TemperatureSensor
from hal.switch.button import Button
from app.fan_control import FanControl


def main(args):
    # Load config
    with open('./config.json') as file:
        config = json.load(file)

    # Load device drivers
    devices = get_devices(config)

    # Register modules
    rtos.register_module('slow_timer', Timer(config.timers.slow.period))
    rtos.register_module('fast_timer', Timer(config.timers.fast.period))
    
    rtos.register_module('temperature_sensor', TemperatureSensor(config.sensors.cpu_temperature, {
        'temperature': devices['temperature_sensor'],
    }))

    rtos.register_module('fan_button', Button(config.buttons.fan_button, {
        'button': devices['fan_button'],
    }))

    # rtos.register_module('alarm_reset_button', Button(config.buttons.alarm_reset_button, {
    #     'button': devices['alarm_reset_button'],
    # }))
    
    rtos.register_module('fan_control', FanControl(config.fan_control, {
        'fan': devices['fan'],
    }))
    
    # rtos.register_module('warning_system', WarningSystem(config.warning_system), {
    #     'led': devices['warning_led']
    # })

    # rtos.register_module('alarm_system', AlarmSystem(config.alarm_system), {
    #     'led0': devices['alarm_led_0'],
    #     'led1': devices['alarm_led_1']
    # })

    # Wire up modules
    rtos.modules['slow_timer'].publish('slow_clock')
    rtos.modules['fast_timer'].publish('fast_clock')

    rtos.modules['temperature_sensor'].subscribe('slow_clock')
    rtos.modules['temperature_sensor'].publish('temperature')

    rtos.modules['fan_button'].subscribe('fast_clock')
    rtos.modules['fan_button'].publish('fan_button')

    # rtos.modules['alarm_reset_button'].subscribe('fast_clock')
    # rtos.modules['alarm_reset_button'].publish('alarm_reset_button')

    rtos.modules['fan_control'].subscribe('slow_clock')
    rtos.modules['fan_control'].subscribe('temperature')
    rtos.modules['fan_control'].subscribe('fan_button')

    # Init modules
    rtos.init_modules()

    # Start event loop
    asyncio.run(rtos.start_event_loop())


if __name__ == '__main__':
    sys.exit(main(sys.argv))