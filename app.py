import sys

from includes.Rental import Rental

app = Rental()

if __name__ == '__main__':

    period = ''
    bikes = 0
    units = 0

    while period not in ["DAY", "HOUR", "WEEK"]:
        period = input("Please, inform period for rental (HOUR/DAY/WEEK):")

    while bikes <= 0:
        bikes_val = input("Now inform the amount of bikes to rent:")
        try:
            bikes = int(bikes_val)
        except ValueError:
            pass

    while units <= 0:
        units_val = input("Last, inform the amount of periods to rent:")
        try:
            units = int(units_val)
        except ValueError:
            pass

    sys.stdout.write('Price: ' + str(app.rent_a_bike(period, units, bikes)))
