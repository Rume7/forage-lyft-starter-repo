from tire_service.TireInterface import TireInterface


class OctoprimeTire(TireInterface):

    def __init__(self, sensor_array):
        if len(sensor_array) == TireInterface.sensor_array_length:
            super().__init__(sensor_array)
        else:
            raise ValueError("Sensor array doesn't have 4 numbers.")

    def needs_service(self):
        return sum(self.get_sensor_array()) >= 3

