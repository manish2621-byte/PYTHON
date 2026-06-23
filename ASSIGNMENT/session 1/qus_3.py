'''Add 2 more song names to my_fav_songs.txt without deleting the existing content, using Python's open() function in append ('a') mode.'''

#open file in append mode
file = open("my_fav_songs.txt","a")

#add 2 new songs (they will be added at the end)

file.write("wildflower\n")
file.write("tere bin\n")


#close the file
file.close()

print("2 songs added  successfully!")