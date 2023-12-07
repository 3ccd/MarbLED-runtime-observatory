import time

import zmq


def pub():
    host = '127.0.0.1'
    port = 5001

    context = zmq.Context()
    sock = context.socket(zmq.REQ)
    sock.connect("tcp://{}:{}".format(host, port))

    time.sleep(1)

    topic = "ANALYZER CAL_LOWER"

    topic = topic.encode('utf-8')

    sock.send_multipart([topic])
    print(sock.recv().decode('utf-8'))

    input("Press Enter to Upper Calibration...")

    topic = "ANALYZER CAL_UPPER"

    topic = topic.encode('utf-8')

    sock.send_multipart([topic])
    print(sock.recv().decode('utf-8'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pub()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

