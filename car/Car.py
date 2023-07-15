from car.Serviceable import Serviceable


class Car(Serviceable):

    def __init__(self, engine, battery, tyre, last_service_date):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre
        self.last_service_date = last_service_date

    def get_engine(self):
        return self.engine

    def get_battery(self):
        return self.battery

    def get_tyre(self):
        return self.tyre

    def needs_service(self):
        return self.engine.needs_service() and self.battery.needs_service()
