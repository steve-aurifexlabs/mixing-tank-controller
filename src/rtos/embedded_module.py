'''Base Embedded Module'''


import asyncio


class EmbeddedModule(object):
    def __init__(self, config, devices):
        self.config = config
        self.devices = devices
        self.state = None
        self.event_attribute_map = {}

    def init_module(self):
        self.queue = asyncio.Queue()
        self.loop = asyncio.get_running_loop()

    async def start_task(self):
        while True:
            event = await self.queue.get()
            
            # Module properties get automatically set with event data
            self[self.event_attribute_map[event.event_name]] = event.value

            while not self.is_idle:
                self.step()

            self.queue.task_done()