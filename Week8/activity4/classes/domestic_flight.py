from classes.passenger_info import PassengerInfo
from classes.flight_type import FlightType
from classes.flight import Flight


class DomesticFlight(PassengerInfo, FlightType):

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        passenger_name,
        ticket_price,
        gate_number
    ):

        Flight.__init__(
            self,
            flight_number,
            origin,
            destination
        )

        self.passenger_name = passenger_name
        self.ticket_price = ticket_price
        self.gate_number = gate_number

    def boarding(self):
        print(f"Boarding at Gate {self.gate_number}")

    def baggage_limit(self):
        print("Baggage Allowance: 23kg")

    def route_type(self):
        print("Domestic Flight")