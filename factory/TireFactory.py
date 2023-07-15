from tire_service.CarriganTire import CarriganTire
from tire_service.OctopimeTire import OctoprimeTire
from tire_service.TireInterface import TireInterface


class TireFactory:

    def create_tire(self, tire_type, sensor_array) -> TireInterface:
        if tire_type == 'Carrigan':
            return CarriganTire(sensor_array)
        elif tire_type == 'Octoprime':
            return OctoprimeTire(sensor_array)
        else:
            raise ValueError("We don't have this tire type for now")

