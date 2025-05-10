# ✅ Purpose:
# You are:

# Given a list of room sizes (sizes)

# Given a list of room requests (requests)

# You need to find the smallest available room that is at least as big as the requested size

# ⚙️ How It Works:
# TreeSet should support ordered storage and efficient search for the next smallest element that meets a condition (like a lower bound).

# Room sizes are stored as (size, counter) pairs to handle duplicates (two rooms with same size).

# For each request, you search for the smallest available room ≥ request.

# If found, you remove it from the set and return the size; otherwise, return 0.

# ✅ Commented Version:
def find_rooms(sizes, requests):
    rooms = TreeSet()     # Create a TreeSet to store room sizes
    counter = 0           # Unique counter to differentiate duplicate sizes
    
    # Add all room sizes to the TreeSet as (size, unique_id) pairs
    for size in sizes:
        counter += 1
        rooms.add((size, counter))
        
    result = []
    for request in requests:
        room = rooms.next((request, 0))  # Find the smallest room >= request
        if room is None:
            result.append(0)  # No suitable room found
        else:
            rooms.remove(room)       # Remove the room from availability
            result.append(room[0])   # Append the room size to the result
            
    return result

