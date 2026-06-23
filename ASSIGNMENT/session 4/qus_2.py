'''Write a function add_song_to_playlist(song_name, playlist) for a Spotify-like app that raises a SongAlreadyExistsError (custom exception) if the song is already present in the playlist.<br><br><em><strong>Hint:</strong> Define SongAlreadyExistsError as a user-defined exception class and use the raise keyword inside your function.</em>'''

# Custom Exception Class
class SongAlreadyExistsError(Exception):
    pass


# Function to add song to playlist
def add_song_to_playlist(song_name, playlist):
    if song_name in playlist:
        raise SongAlreadyExistsError(
            f"'{song_name}' already exists in the playlist!"
        )

    playlist.append(song_name)
    print(f"'{song_name}' added successfully.")


# Example Playlist
playlist = ["Believer", "Perfect", "Kesariya"]

try:
    add_song_to_playlist("Believer", playlist)  # Already exists
    # add_song_to_playlist("Shape of You", playlist)  # New song

except SongAlreadyExistsError as e:
    print("Error:", e)

print("Playlist:", playlist)