'''Run a dummy load in 4 processes to heat up the chipset'''


import os


def heat_cpu():
    a = 0

    os.fork()
    os.fork()

    while True:
        a += 1

if __name__ == '__main__':
    heat_cpu()