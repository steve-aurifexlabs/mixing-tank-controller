'''Ring Buffer'''


import json


class RingBuffer(object):
    '''Almost a ring buffer - TODO'''

    def __init__(self, size):
        self.max_length = size
        self.buffer = []

    def append(self, obj):
        self.buffer.append(obj)
        if(len(self.buffer) > self.max_length):
            self.buffer.pop(0)

    def __repr__(self):
        return json.dumps(self.buffer)

    def __getattr__(self, name):
        return self.buffer[name]

    def __setattr__(self, name, value):
        self.buffer[name] = value