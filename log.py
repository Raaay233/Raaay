import time
import sys


class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.terminal.flush()
        self.log.write(message)
        self.log.flush()


sys.stdout = Logger('test.log', sys.stdout)
sys.stderr = Logger('test.log', sys.stderr)

for i in range(10):
    print(i)
    time.sleep(1)

