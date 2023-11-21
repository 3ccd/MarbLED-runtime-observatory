import socket
import time

import numpy as np


class SendColor:
    ip = None
    sock = None
    chain = None

    def __init__(self, ip, chain):
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.chain = chain

    def set_color(self, color):
        cm = np.full(288, color, dtype=np.uint32)

        for i in range(self.chain):
            self.sock.sendto(cm.tobytes(), (self.ip, 8002 + i))

    def __del__(self):
        self.sock.close()


if __name__ == '__main__':
    sc = SendColor('192.168.101', 2)
    sc.set_color(0x10000000)
    time.sleep(2)
    sc.set_color(0x00000000)
