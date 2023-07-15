from tire_service.TireInterface import TireInterface


class CarriganTire(TireInterface):

    def __init__(self, sensor_array):
        if len(sensor_array) == TireInterface.sensor_array_length:
            super().__init__(sensor_array)
        else:
            raise ValueError("Sensor array doesn't have 4 numbers.")

    def needs_service(self):
        for value in self.get_sensor_array():
            if value >= 0.9:
                return True
        return False
