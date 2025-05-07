
def max_customers(arrivals, departures):
    events = []

    # Convert arrival times into events with a flag (1 for arrival)
    for time in arrivals:
        events.append((time, 1))

    # Convert departure times into events with a flag (2 for departure)
    for time in departures:
        events.append((time, 2))

    # Sort all events: arrivals and departures
    # Python tuples are sorted by first element, and then second, 
    # so arrivals (1) will come before departures (2) if times are equal
    events.sort()

    counter = 0   # Current number of customers in the shop
    result = 0    # Maximum number of customers at any time

    # Process all events in order
    for event in events:
        if event[1] == 1:    # Arrival
            counter += 1
        if event[1] == 2:    # Departure
            counter -= 1

        # Update maximum seen so far
        result = max(result, counter)

    return result
