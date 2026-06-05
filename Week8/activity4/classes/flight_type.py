from classes.flight import Flight


class FlightType(Flight):

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        ticket_price
    ):
        super().__init__(flight_number, origin, destination)
        self.ticket_price = ticket_price

    def calculate_fare(self):
        return self.ticket_price

    def apply_discount(self, discount):
        return self.ticket_price - discount

    def fare_details(self):
        print(f"Ticket Price: ${self.ticket_price}")