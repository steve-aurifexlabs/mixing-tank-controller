'''Button module'''


from rtos.embedded_module import EmbeddedModule


class Button(EmbeddedModule):
    def __init__(self, config, devices):
        super().__init__(config, devices)
        self.value = None

    def init_module(self):
        super().init_module()
        self.value = self.devices["button"]["read"]()

    def step(self):
        self.value = self.devices["button"]["read"]()
        
        self.send({
            'value': self.value,
        })
        
        self.is_idle = True
