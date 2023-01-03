'''Timer'''

import asyncio
from rtos.embedded_module import EmbeddedModule


class Timer(EmbeddedModule):
    def __init__(self, interval):
        super().__init__({}, {})
        
        self.interval = interval / 1000.0
        self.loop = None
        self.time = None
        self.is_timer = True

    def init_module(self):
        super().init_module()

    async def start_task(self):
        self.loop = asyncio.get_running_loop()
        self.time = self.loop.time()

    async def tick(self):
        if not self.loop:
            self.loop = asyncio.get_running_loop()
            self.time = self.loop.time()
            
        print(self, self.loop.time(), self.time, self.interval)
        
        if(self.loop.time() - self.time > self.interval):
            self.time = self.loop.time()
            self.loop.create_task(self.send({}))