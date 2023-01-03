

class Led(object):
    def __init__(self, config, devices):
        self.config = config
        self.devices = devices

    def init_module(self):
        pass

    def off(self):
        self.devices["led"].write(False)

    def on(self):
        self.devices["led"].write(True)