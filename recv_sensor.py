import socket
import numpy as np


class TcpSensor:
    s: socket = None

    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        print("connect sensor port")

    def get(self, sensors):
        ret = self.s.recv(sensors * 2)
        return np.frombuffer(ret, dtype=np.uint16)

    def __del__(self):
        self.s.close()


if __name__ == '__main__':
    ts = TcpSensor('192.168.0.101', 8004)
    while True:
        arr = ts.get(36)
        print('ArrLength: {}, No.0_Data: {}'.format(arr.shape, arr[18]))
