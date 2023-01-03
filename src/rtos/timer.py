'''Timer'''


from rtos.embedded_module import EmbeddedModule


class Timer(EmbeddedModule):
    def __init__(self, interval):
        super().__init__({}, {})
        
        self.interval = interval
        self.loop = None
        self.time = None
        self.is_timer = True

    def init_module(self):
        super().init_module()
        self.time = self.loop.time()

    def tick(self):
        if(self.loop.time() - self.time > self.interval):
            self.time = self.loop.time()
            self.send({})