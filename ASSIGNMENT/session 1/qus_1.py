'''Create a text file named my_fav_songs.txt using Python's open() function in write ('w') mode, and write the names of your 5 favorite songs into it, each on a new line.'''
# open file in write mode
file = open ("my_fav_songs.txt","w")

#write 5 favorite songs (you can change names)

file.write("tum hi ho\n")
file.write("tuje sochta hu\n")
file.write("lovely\n")
file.write("perfect\n")


#close the file
file.close()

print("FILE CREATED AND SONGS WRITTEN SUCESSFULLY")