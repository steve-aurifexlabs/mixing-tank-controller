

class Button(object):
    def __init__(self, config, devices):
        self.config = config
        self.devices = devices

        self.value = None

    def init_module(self):
        self.value = self.devices["button"].read()

    def step(self):
        self.value = self.devices["button"].read()
        
        self.send({
            'value': self.value,
        })
        
        self.is_idle = True
