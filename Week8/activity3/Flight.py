# ==================================================
# Parent Class: Flight
# Represents a general flight in Air New Zealand
# ==================================================

class Flight:
    
    # Constructor to initialize common flight details
    def __init__(self, flight_number, origin, destination, departure_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time

    # Method to display general flight information
    def display_flight_info(self):
        print("Flight Number :", self.flight_number)
        print("Origin        :", self.origin)
        print("Destination   :", self.destination)
        print("Departure Time:", self.departure_time)

    # Common method shared by all flight types
    def get_duration(self):
        print("Duration information available in the flight system.")


# ==================================================
# Child Class: DomesticFlight
# Inherits from Flight
# Represents Air New Zealand domestic flights
# ==================================================

class DomesticFlight(Flight):

    # Constructor
    def __init__(self, flight_number, origin, destination,
                 departure_time, terminal_number, baggage_limit):

        # Call the parent class constructor
        super().__init__(
            flight_number,
            origin,
            destination,
            departure_time
        )

        # Attributes specific to domestic flights
        self.terminal_number = terminal_number
        self.baggage_limit = baggage_limit

    # Method specific to domestic flights
    def display_domestic_details(self):
        print("Terminal Number :", self.terminal_number)
        print("Baggage Limit   :", self.baggage_limit, "kg")


# ==================================================
# Main Program
# ==================================================

# Create a DomesticFlight object
flight1 = DomesticFlight(
    flight_number="NZ101",
    origin="Auckland",
    destination="Wellington",
    departure_time="08:30 AM",
    terminal_number=2,
    baggage_limit=23
)

print("=== Air New Zealand Domestic Flight Information ===\n")

# Inherited method from Flight class
flight1.display_flight_info()

print()

# Inherited method from Flight class
flight1.get_duration()

print()

# Method specific to DomesticFlight class
flight1.display_domestic_details()