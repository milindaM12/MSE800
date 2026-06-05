from classes.flight import Flight


class PassengerInfo(Flight):

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        passenger_name
    ):
        super().__init__(flight_number, origin, destination)
        self.passenger_name = passenger_name

    def add_passenger(self):
        print(f"{self.passenger_name} added successfully")

    def remove_passenger(self):
        print(f"{self.passenger_name} removed successfully")

    def passenger_info(self):
        print(f"Passenger: {self.passenger_name}")