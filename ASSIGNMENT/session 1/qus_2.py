'''Write a Python script that opens the my_fav_songs.txt file in read ('r') mode and prints each song name to the console with its line number (like a playlist).'''

#open the file in read mode
file = open("my_fav_songs.txt","r")
#read all lines
songs = file.readlines()

#print each song with line number
for index,song in enumerate(songs,start=1):
    print(f"{index}.{song.strip()}")


#close the file
file.close()