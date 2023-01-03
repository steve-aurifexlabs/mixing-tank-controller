'''Temperature sensor module'''


from rtos.embedded_module import EmbeddedModule


class TemperatureSensor(EmbeddedModule):
    def __init__(self, config, devices):
        self.config = config
        self.devices = devices

        self.temperature = None

    def init_module(self):
        self.temperature = self.devices["temperature"].read()

    def step(self):
        self.temperature = self.devices["temperature"].read()
        
        self.send({
            'temperature': self.temperature,
        })
        
        self.is_idle = True
