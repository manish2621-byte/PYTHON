'''Build a script that reads all lines from my_fav_songs.txt, counts how many songs are listed, and displays 'Total songs: X' at the end.<br><br><em><strong>Hint:</strong> Use the readlines() method to get all lines as a list and len() to count.</em>'''

#open file in read mode
file = open("my_fav_songs.txt","r")
# read all lines into a list
songs = file.readlines()
#close the file
file.close()
#count total songs
total_songs = len(songs)

#display result
print("total songs:", total_songs)