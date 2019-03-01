__author__ = 'zhengwang'

import socket
import time
import struct


class SensorStreamingTest(object):
    def __init__(self, host, port):

        self.server_socket = socket.socket()
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)
        self.connection, self.client_address = self.server_socket.accept()
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.streaming()

    def streaming(self):

        try:
            print("Host: ", self.host_name + ' ' + self.host_ip)
            print("Connection from: ", self.client_address)
            start = time.time()

            while True:
                data_bytes = self.connection.recv(1024)
                sensor_data = struct.unpack('!d', data_bytes)
                print("Distance: {:.2f}".format(sensor_data[0]))
                #print ((sensor_data[0]))
                #print("Distance: %0.1f cm" % x)
                
                # test for 10 seconds
                if time.time() - start > 10:
                    break
        finally:
            self.connection.close()
            self.server_socket.close()


if __name__ == '__main__':
    h, p = "192.168.0.5", 8002
    SensorStreamingTest(h, p)
