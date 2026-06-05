from classes.passenger_info import PassengerInfo
from classes.flight_type import FlightType
from classes.flight import Flight


class InternationalFlight(PassengerInfo, FlightType):

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        passenger_name,
        ticket_price,
        passport_required
    ):

        Flight.__init__(
            self,
            flight_number,
            origin,
            destination
        )

        self.passenger_name = passenger_name
        self.ticket_price = ticket_price
        self.passport_required = passport_required

    def visa_check(self):
        print("Visa verification completed")

    def customs_info(self):
        print("Customs declaration required")

    def route_type(self):
        print("International Flight")