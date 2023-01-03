'''Temperature sensor module'''


import asyncio
from rtos.embedded_module import EmbeddedModule


class TemperatureSensor(EmbeddedModule):
    def __init__(self, config, devices):
        super().__init__(config, devices)
        self.temperature = None

    def init_module(self):
        super().init_module()
        self.temperature = self.devices["temperature"]["read"]()

    async def step(self):
        if not self.loop:
            self.loop = asyncio.get_running_loop()

        self.temperature = self.devices["temperature"]["read"]()
        
        self.loop.create_task(self.send({
            'temperature': self.temperature,
        }))
        
        self.is_idle = True
