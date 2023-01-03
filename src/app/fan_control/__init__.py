'''Fan Control Module'''


from pprint import pprint

from rtos.embedded_module import EmbeddedModule
from hal.actuator.fan import Fan


class FanControl(EmbeddedModule):
    def __init__(self, config, devices):
        super().__init__(config, devices)

        self.state = None
        self.is_idle = None

        # Maps event names to module properties
        self.event_attribute_map = {
            'slow_clock': 'slow_clock',
            'temperature': 'temperature',
            'fan_button': 'button_pressed',
        }

        self.fan = Fan(self.config["fan"], {
            'fan': devices['fan'],
        })

    def init_module(self):
        super().init_module()
        
        self.state = 'FAN_OFF'
        self.is_idle = True

    def step(self):
        pprint(self)
        def fan_off():
            self.fan.off()
            if self.button_pressed or (self.temperature >= self.config.FAN_TEMP):
                self.state = 'FAN_STARTING'
            else:
                self.is_idle = True

        def fan_starting():
            self.fan.on()
            if self.loop.time() - self.fan_timer > self.config.FAN_START_TIME:
                self.state = 'FAN_ON'
            else:
                self.is_idle = True

        def fan_on():
            self.fan.on()
            if self.button_pressed and (self.temperature < self.config.FAN_TEMP):
                self.state = 'FAN_STOPPING'
            else:
                self.is_idle = True

        def fan_stopping():
            self.fan.off()
            if self.temperature >= self.config.FAN_TEMP:
                self.state = 'FAN_STARTING'
            elif self.loop.time() - self.fan_timer > self.config.FAN_START_TIME:
                self.state = 'FAN_OFF'
            else:
                self.is_idle = True
        
        state_machine = {
            "FAN_OFF": fan_off,
            "FAN_STARTING": fan_starting,
            "FAN_ON": fan_on,
            "FAN_STOPPING": fan_stopping,
        }

        state_machine[self.state]()