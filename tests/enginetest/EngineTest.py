import unittest
from datetime import datetime

from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine


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

    def test_willoughby_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        current_mileage = 70200
        last_service_mileage = 10000

        willoughby_engine = WilloughbyEngine(last_service_date, last_service_mileage, current_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        current_mileage = 86000
        last_service_mileage = 51000

        willoughby_engine = WilloughbyEngine(last_service_date, last_service_mileage, current_mileage)
        self.assertFalse(willoughby_engine.needs_service())

    def test_willoughby_engine_negative_mileage_difference(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        current_mileage = 51200
        last_service_mileage = 73000

        capulet_engine = CapuletEngine(last_service_date, last_service_mileage, current_mileage)

        with self.assertRaises(ValueError):
            capulet_engine.needs_service()

    def test_sternman_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        warning_light_on = True

        sternman_engine = SternmanEngine(last_service_date, warning_light_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        warning_light_on = False

        sternman_engine = SternmanEngine(last_service_date, warning_light_on)
        self.assertFalse(sternman_engine.needs_service())

    def test_sternman_engine_negative_mileage_difference(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        warning_light_on = "True"

        sternman_engine = SternmanEngine(last_service_date, warning_light_on)

        with self.assertRaises(ValueError):
            sternman_engine.needs_service()
