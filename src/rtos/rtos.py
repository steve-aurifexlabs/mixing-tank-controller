'''Core embedded system layer'''


import asyncio
import gc

from rtos.ring_buffer import RingBuffer


modules = {}
timers = []
devices = {}
event_routes = {}

# tickStats = RingBuffer(1000)


def register_module(module_name, module):
    module.name = module_name

    def publish(event_name):
        module.published_event = event_name
        event_routes[event_name] = {
            "publisher": module,
            "subscribers": [],
        }

    def subscribe(event_name):
        event_routes[event_name]["subscribers"].append(module)

    async def send(data):
        subscribers = event_routes[module.published_event]["subscribers"]
        for subscriber in subscribers:
            await subscriber.queue.put({
                'event_name': module.published_event,
                'value': data,
            })

    module.publish = publish
    module.subscribe = subscribe
    module.send = send
    
    modules[module.name] = module

    if module.is_timer:
        timers.append(module)

def init_modules():
    for module in modules.values():
        module.init_module()

async def start_event_loop():
    loop = asyncio.get_running_loop()

    for module in modules.values():
        if not module.is_timer:
            loop.create_task(module.start_task())

    print('\n---Start Scheduler---\n')
    while True:
        # startTickTime = loop.time()

        # tickStats.add({})

        for timer in timers:
            await timer.tick()

        # tickStats[-1].cpuTime = loop.time() - startTickTime

        # gc.collect(0)

        # tickStats[-1].gcTime = loop.time() - startTickTime - tickStats.cpuTime
        
        await asyncio.sleep(0.010)