'''Ring Buffer'''


import json


class RingBuffer(object):
    '''Almost a ring buffer - TODO'''

    def __init__(self, size):
        self.max_length = size
        self.buffer = []

    def add(self, obj):
        self.buffer.append(obj)
        if(self.buffer.length > self.max_length):
            self.buffer.pop(0)

    def __repr__(self):
        return json.dumps(self.buffer)
