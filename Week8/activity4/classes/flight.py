# Parent Class

class Flight:

    def __init__(self, flight_number, origin, destination):
        self.airline = "Air New Zealand"
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination

    def display_info(self):
        print(f"\nAirline: {self.airline}")
        print(f"Flight Number: {self.flight_number}")
        print(f"Origin: {self.origin}")
        print(f"Destination: {self.destination}")

    def update_route(self, new_destination):
        self.destination = new_destination
        print(f"Destination updated to {new_destination}")

    def flight_status(self):
        print("Status: On Time")