'''Simulate a Zomato-style order history: create a file orders.txt with at least 5 lines (each line is an order). Write a script that reads and prints each order line-by-line using a loop, and after reading each line, prints the file pointer's position using tell().'''

#create file with 5 orders
file =open("orders.txt","w")

file.write("order 1: pizza margherita\n")
file.write("order 2:burger combo\n")
file.write("order3: biryani special\n")
file.write("order 4: pasta alfredo\n")
file.write("order 5: ice cream sundae\n")

file.close()