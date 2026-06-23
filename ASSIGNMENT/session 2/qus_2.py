'''Write a function read_next_line(filename) that opens a file, moves the file pointer to the 20th byte using seek(), and prints the next line from that position.<br><br><em><strong>Hint:</strong> Use seek(20) before calling readline().</em>'''

def read_next_line(filename):
    #open file in read mode
    file = open(filename,"r")

    #move file pointer to 20th byte
    file.seek(20)

    #read and print the next line from that position
    line = file.readline()
    print(line)

    file.close()

    #example usage
    read_next_line("lyrics.txt")