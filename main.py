# This is a sample Python script.
import time
import numpy as np
import cv2

import zmq


def pub():
    host = '127.0.0.1'
    port = 8002
    bid = 1

    topic = 'BRD_COLOR {}'.format(bid)
    topic = topic.encode('utf-8')

    cap = cv2.VideoCapture('test.mp4')

    context = zmq.Context()

    sock = context.socket(zmq.PUB)
    sock.bind("tcp://{}:{}".format(host, port))

    time.sleep(1)

    while True:
        ret, frame = cap.read()
        resized = cv2.resize(frame, (18, 18))

        resized = resized * 0.1
        resized = resized.astype(np.uint8)

        # r = np.zeros((18, 18), dtype=np.uint8)
        r = resized[:, :, 0]

        # g = np.zeros((18, 18), dtype=np.uint8)
        g = resized[:, :, 1]

        # b = np.zeros((18, 18), dtype=np.uint8)
        b = resized[:, :, 2]

        sock.send_multipart([topic, r.flatten().tobytes(), g.flatten().tobytes(), b.flatten().tobytes()])

        cv2.imshow('test', frame)
        ret = cv2.waitKey(33)
        if ret == ord('q'):
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pub()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
