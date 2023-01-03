'''Core embedded system layer'''


import asyncio
import gc

from rtos.ring_buffer import RingBuffer


modules = []
timers = []
devices = {}
event_routes = {}

tickStats = RingBuffer(1000)


def register_module(module_name, module):
    module.name = module_name

    def publish(event_name):
        module.published_event = event_name
        event_routes[event_name] = {
            "publisher": module,
            "subscribers": [],
        }

    def subscribe(event_name):
        event_routes[event_name].subscribers.add(module)

    def send(data):
        subscribers = event_routes[module.published_event].subscribers
        for subscriber in subscribers:
            subscriber.queue.put({
                'event_name': module.published_event,
                'value': data,
            })

    module.publish = publish
    module.subscribe = subscribe
    module.send = send
    
    modules.add(module)

    if module.is_timer:
        timers.add(module)

def init_modules():
    for module in modules:
        module.init_module()

async def start_event_loop():
    loop = asyncio.get_running_loop()

    for module in modules:
        if not module.is_timer:
            module.start_task()

    while True:
        startTickTime = loop.time()

        tickStats.add({})

        for timer in timers:
            timer.tick()

        tickStats[-1].cpuTime = loop.time() - startTickTime

        gc.collect(0)

        tickStats[-1].gcTime = loop.time() - startTickTime - tickStats.cpuTime
        
        await asyncio.sleep(1)