from classes.domestic_flight import DomesticFlight
from classes.international_flight import InternationalFlight


print("===== DOMESTIC FLIGHT =====")

domestic = DomesticFlight(
    "NZ101",
    "Auckland",
    "Wellington",
    "John Smith",
    199,
    "A5"
)

domestic.display_info()
domestic.passenger_info()
domestic.fare_details()
domestic.boarding()
domestic.baggage_limit()
domestic.route_type()

print("\n===== INTERNATIONAL FLIGHT =====")

international = InternationalFlight(
    "NZ201",
    "Auckland",
    "Sydney",
    "Sarah Lee",
    699,
    True
)

international.display_info()
international.passenger_info()
international.fare_details()
international.visa_check()
international.customs_info()
international.route_type()