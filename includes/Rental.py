class Rental:
    base_prices = {'HOUR': 5.0, 'DAY': 20.0, 'WEEK': 60.0}

    def rent_a_bike(self, rent_type, time_units, bikes_amount):
        if rent_type not in ['HOUR', 'DAY', 'WEEK']:
            raise ValueError('Invalid rent_type value')

        if time_units <= 0:
            raise ValueError('Invalid time_units value')

        if bikes_amount <= 0:
            raise ValueError('Invalid bikes_amount value')

        rent_value = self.base_prices[rent_type]

        discount = 1
        if 3 <= bikes_amount <= 5:
            discount = 0.7

        return round(bikes_amount * time_units * rent_value * discount, 2)
