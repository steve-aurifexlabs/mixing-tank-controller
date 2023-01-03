
class Fan(object):
    def __init__(self, config, devices):
        self.config = config
        self.devices = devices

    def init_module(self):
        pass

    def off(self):
        self.devices["fan"].write(False)

    def on(self):
        self.devices["fan"].write(True)