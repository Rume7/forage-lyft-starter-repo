from car import Car, Calliope, Glissade, Palindrome, Rorschach, Thovex
from ICarFactory import ICarFactory
from factory import TireFactory, EngineFactory, BatteryFactory


class CarFactory(ICarFactory):

    @staticmethod
    def create_a_car(car_type, engine_type, battery_type, last_service_date, last_service_mileage,
                     current_mileage, current_date, warning_light_on,
                     tire_type, sensor_array) -> Car:

        an_engine = EngineFactory.create_engine(engine_type, last_service_mileage, current_mileage, warning_light_on)
        a_battery = BatteryFactory.create_battery(battery_type, last_service_date, current_date)
        a_tyre = TireFactory.create_tire(tire_type, sensor_array)

        if car_type.capitalize() == 'Calliope':
            return Calliope(an_engine, a_battery, a_tyre, last_service_date)
        elif car_type.capitalize() == 'Glissade':
            return Glissade(an_engine, a_battery, a_tyre, last_service_date)
        elif car_type.capitalize() == 'Palindrome':
            return Palindrome(an_engine, a_battery, a_tyre, last_service_date)
        elif car_type.capitalize() == 'Rorschach':
            return Rorschach(an_engine, a_battery, a_tyre, last_service_date)
        elif car_type.capitalize() == 'Thovex':
            return Thovex(an_engine, a_battery, a_tyre, last_service_date)
        else:
            raise ValueError("Wrong type of car.")
