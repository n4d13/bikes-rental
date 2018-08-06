import unittest

from includes.Rental import Rental


class RentalTest(unittest.TestCase):

    def test_one_bike_one_hour(self):
        app = Rental()
        price = app.rent_a_bike('HOUR', 1, 1)
        self.assertTrue(5 == price, "Wrong price for rental of 1 bike 1 hour")

    def test_two_bikes_one_hour(self):
        app = Rental()
        price = app.rent_a_bike('HOUR', 1, 2)
        self.assertTrue(10 == price, "Wrong price for rental of 2 bikes 1 hour")

    def test_tree_bikes_one_hour(self):
        app = Rental()
        price = app.rent_a_bike('HOUR', 1, 3)
        self.assertTrue(10.5 == price, "Wrong price for rental of 3 bikes 1 hour")

    def test_one_bike_one_day(self):
        app = Rental()
        price = app.rent_a_bike('DAY', 1, 1)
        self.assertTrue(20 == price, "Wrong price for rental of 1 bike 1 day")

    def test_two_bikes_one_day(self):
        app = Rental()
        price = app.rent_a_bike('DAY', 1, 2)
        self.assertTrue(40 == price, "Wrong price for rental of 2 bikes 1 day")

    def test_tree_bikes_one_day(self):
        app = Rental()
        price = app.rent_a_bike('DAY', 1, 3)
        self.assertTrue(42 == price, "Wrong price for rental of 3 bikes 1 day")

    def test_one_bike_one_week(self):
        app = Rental()
        price = app.rent_a_bike('WEEK', 1, 1)
        self.assertTrue(60 == price, "Wrong price for rental of 1 bike 1 week")

    def test_two_bikes_one_week(self):
        app = Rental()
        price = app.rent_a_bike('WEEK', 1, 2)
        self.assertTrue(120 == price, "Wrong price for rental of 2 bikes 1 week")

    def test_tree_bikes_one_week(self):
        app = Rental()
        price = app.rent_a_bike('WEEK', 1, 3)
        self.assertTrue(126 == price, "Wrong price for rental of 3 bikes 1 week")

    def test_invalid_bikes_amount_should_fail(self):
        app = Rental()
        self.assertRaises(ValueError, app.rent_a_bike, "HOUR", 1, 0)

    def test_invalid_units_amount_should_fail(self):
        app = Rental()
        self.assertRaises(ValueError, app.rent_a_bike, "HOUR", 0, 1)

    def test_invalid_type_should_fail(self):
        app = Rental()
        self.assertRaises(ValueError, app.rent_a_bike, "MONTH", 1, 1)
