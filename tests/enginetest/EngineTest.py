import unittest
from datetime import datetime

from engine.CapuletEngine import CapuletEngine


class TestEngine(unittest.TestCase):
    
    def test_capulet_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        current_mileage = 40200
        last_service_mileage = 10000

        capulet_engine = CapuletEngine(last_service_date, last_service_mileage, current_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        current_mileage = 40200
        last_service_mileage = 23000

        capulet_engine = CapuletEngine(last_service_date, last_service_mileage, current_mileage)
        self.assertFalse(capulet_engine.needs_service())

    def test_capulet_engine_negative_mileage_difference(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        current_mileage = 40200
        last_service_mileage = 43000

        capulet_engine = CapuletEngine(last_service_date, last_service_mileage, current_mileage)

        with self.assertRaises(ValueError):
            capulet_engine.needs_service()