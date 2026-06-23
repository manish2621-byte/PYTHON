'''Create a function book_movie_ticket that takes the number of tickets as input and divides a fixed wallet balance by the number of tickets to get the price per ticket. Handle ZeroDivisionError and ValueError using multiple except blocks, and print a different message for each error.<br><br><em><strong>Hint:</strong> Use two separate except blocks for ZeroDivisionError and ValueError.</em>'''

def book_movie_ticket():
    wallet_balance = 1000  # Fixed wallet balance

    try:
        tickets = int(input("Enter number of tickets: "))

        price_per_ticket = wallet_balance / tickets

        print("Price per ticket:", price_per_ticket)

    except ZeroDivisionError:
        print("Error: Number of tickets cannot be zero!")

    except ValueError:
        print("Error: Please enter a valid numeric value!")


# Call the function
book_movie_ticket()