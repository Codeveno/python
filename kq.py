

class FlightBookingApp:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight_number, destination, departure_time):
        flight = {
            "flight_number": flight_number,
            "destination": destination,
            "departure_time": departure_time,
        }
        self.flights.append(flight)
        print(f"Flight {flight_number} to {destination} added.")

    def book_flight(self, flight_number):
        for flight in self.flights:
            if flight["flight_number"] == flight_number:
                print(f"Flight {flight_number} to {flight['destination']} booked!")
                return
        print(f"Flight {flight_number} not found.")

    def display_flights(self):
        if not self.flights:
            print("No flights available.")
        else:
            print("Available Flights:")
            for flight in self.flights:
                print(f"Flight {flight['flight_number']} to {flight['destination']} at {flight['departure_time']}")

    
app = FlightBookingApp()
app.add_flight("KQ101", "Nairobi", "10:00 AM")
app.add_flight("KQ202", "New York", "12:00 PM")
app.display_flights()
app.book_flight("KQ101")