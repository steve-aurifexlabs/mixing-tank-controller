'''Base gpio using python-periphery'''


from periphery import GPIO


class GpioIn(object):
    def __init__(self, config):
        self.config = config
        print(config)
        self.device = GPIO('/dev/gpiochip' + config["chip"], config["line"], 'in')

    def read(self):
        return self.device.read()

class GpioOut(object):
    def __init__(self, config):
        self.config = config
        self.device = GPIO('/dev/gpiochip' + config["chip"], config["line"], 'out')

    def write(self, value):
        self.device.write(value)