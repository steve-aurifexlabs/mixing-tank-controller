'''Base Embedded Module'''


import json
from pprint import pprint
import asyncio


class EmbeddedModule(object):
    def __init__(self, config, devices):
        self.config = config
        self.devices = devices
        self.state = None
        self.event_attribute_map = {}
        self.is_timer = False
        self.is_idle = True

    def init_module(self):
        pass

    async def start_task(self):
        self.queue = asyncio.Queue()
        self.loop = asyncio.get_running_loop()

        while True:
            event = await self.queue.get()
            
            print('Event: ', json.dumps(event))

            # Module properties get automatically set with event data
            try:
                self[self.event_attribute_map[event["event_name"]]] = event["value"]
            except:
                pass

            self.is_idle = False
            while not self.is_idle:
                await self.step()

            self.queue.task_done()
