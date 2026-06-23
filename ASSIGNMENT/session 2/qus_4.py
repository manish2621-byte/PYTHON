'''Given a file called playlist.txt containing song names (one per line), write code to jump to the start of the third song using seek() and readline(), then print only that song's name.<br><br><em><strong>Constraint:</strong> Do not read the whole file into memory at once.</em>'''
# Step 1: Create playlist.txt
file = open("playlist.txt", "w")

file.write("Tum Hi Ho\n")
file.write("Kesariya\n")
file.write("Believer\n")
file.write("Perfect\n")
file.write("Shape of You\n")

file.close()


# Step 2: Open the file for reading
file = open("playlist.txt", "r")

# Skip first song
file.readline()

# Skip second song
file.readline()

# Get position of third song
position = file.tell()

# Move pointer to that position
file.seek(position)

# Read and print the third song
third_song = file.readline()

print("Third song:", third_song.strip())

file.close()