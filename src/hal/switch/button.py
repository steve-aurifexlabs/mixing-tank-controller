'''Button module'''


import asyncio
from rtos.embedded_module import EmbeddedModule


class Button(EmbeddedModule):
    def __init__(self, config, devices):
        super().__init__(config, devices)
        self.value = None

    def init_module(self):
        super().init_module()
        self.value = self.devices["button"]["read"]()

    async def step(self):
        if not self.loop:
            self.loop = asyncio.get_running_loop()

        self.value = self.devices["button"]["read"]()
        
        self.loop.create_task(self.send({
            'value': self.value,
        }))
        
        self.is_idle = True
