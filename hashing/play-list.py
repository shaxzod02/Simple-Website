
#✅ max_length function explanation:
def max_length(songs):
    n = len(songs)  # Get the length of the 'songs' list
    
    pos = {}         # Dictionary to store the most recent position of each song
    start = 0        # Starting index of the current sublist without duplicates
    length = 0       # Variable to store the maximum length of sublist without duplicates
    
    for i, song in enumerate(songs):  # Iterate through the 'songs' list with index 'i'
        if song in pos:  # If the song is already in the dictionary (i.e., it was seen before)
            # Move the starting index 'start' right after the previous occurrence of this song
            start = max(start, pos[song] + 1)
        
        # Calculate the length of the current sublist and update 'length' if it's greater
        length = max(length, i - start + 1)
        
        # Update the position of the current song in the dictionary
        pos[song] = i
    
    return length  # Return the length of the longest sublist without duplicate songs

# Explanation:
# pos dictionary: This stores the most recent index (position) of each song encountered in the list. This allows us to quickly check if we've seen a song before and where its last occurrence was.

# start pointer: This keeps track of the start of the current sublist (from start to i) without any duplicates. If a duplicate song is encountered, we update start to be one index after the previous occurrence of that song.

# length variable: This stores the maximum length of a sublist encountered that does not contain duplicate songs. Every time we find a valid sublist, we compare its length to the current maximum and update length accordingly.

# # enumerate(songs): We use enumerate to get both the index i and the song itself (song) during the iteration.