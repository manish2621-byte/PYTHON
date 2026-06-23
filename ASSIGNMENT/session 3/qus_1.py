'''Write a Python function get_song_duration that takes a song name and returns its duration from a predefined dictionary. Use a try-except block to handle the case where the song is not found and print 'Song not found on Spotify!'.'''
# Step 1: Create a file with song names
file = open("songs.txt", "w")

file.write("Believer\n")
file.write("Perfect\n")
file.write("Kesariya\n")
file.write("Tum Hi Ho\n")
file.write("Shape of You\n")

file.close()


# Step 2: Function to get song duration
def get_song_duration(song_name):
    songs = {
        "Believer": "3:24",
        "Perfect": "4:23",
        "Kesariya": "4:28",
        "Tum Hi Ho": "4:22",
        "Shape of You": "3:53"
    }

    try:
        duration = songs[song_name]
        print(f"{song_name} duration: {duration}")
    except KeyError:
        print("Song not found on Spotify!")


# Step 3: Test the function
get_song_duration("Believer")
get_song_duration("Despacito")