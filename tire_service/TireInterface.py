from abc import ABCMeta, abstractmethod


class TireInterface(metaclass=ABCMeta):

    sensor_array_length = 4

    def __init__(self, sensor_array):
        self.sensor = [elem for elem in sensor_array]

    def get_sensor_array(self):
        return self.sensor

    @abstractmethod
    def needs_service(self):
        pass
