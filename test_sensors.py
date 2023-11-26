import os
import time
import numpy as np

import recv_sensor, send_color

sample_count = 100

save_data_prefix = "cover-off_marble-on_IR-on_" + str(time.time())
os.makedirs("temp/{}".format(save_data_prefix), exist_ok=True)

color_table = [
    0x00000000,
    0x10000000,
    0x30000000,
    0x60000000,
    0x00100000,
    0x00300000,
    0x00600000,
    0x00001000,
    0x00003000,
    0x00006000
]
sensor_data = np.empty([0, 36], dtype=np.uint16)

rs = recv_sensor.TcpSensor('192.168.0.101', 8004)
sc = send_color.SendColor('192.168.0.101', 2)

for i in range(len(color_table)):
    sensor_data = np.empty([0, 36], dtype=np.uint16)

    sc.set_color(color_table[i])
    time.sleep(2)

    for j in range(sample_count):
        ret = rs.get(36)
        sensor_data = np.append(sensor_data, ret.reshape((1, 36)), axis=0)

    print('--------- Test: {} ----------'.format(i))
    print(np.mean(sensor_data, axis=0))
    print(np.std(sensor_data, axis=0))
    np.savetxt('temp/{}/{}.csv'.format(save_data_prefix, i), sensor_data)

sc.set_color(0x00000000)
