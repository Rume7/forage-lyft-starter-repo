import unittest
from datetime import datetime

from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery


class BatteryTest(unittest.TestCase):

    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_year = today.year - 4
        last_service_date = today.replace(last_service_year, today.month, today.day)
        nubbin_battery = NubbinBattery(last_service_date, today)

        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_year = today.year - 6
        last_service_date = today.replace(last_service_year, today.month, today.day)
        nubbin_battery = NubbinBattery(last_service_date, today)

        self.assertFalse(nubbin_battery.needs_service())

    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_year = current_date.year - 8
        last_service_date = current_date.replace(last_service_year, current_date.month, current_date.day)

        spindler = SpindlerBattery(last_service_date, current_date)

        self.assertTrue(spindler.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_year = current_date.year - 5
        last_service_date = current_date.replace(last_service_year, current_date.month, current_date.day)

        spindler = SpindlerBattery(last_service_date, current_date)

        self.assertFalse(spindler.needs_service())
