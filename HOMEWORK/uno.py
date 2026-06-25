import tkinter as tk
import random

# Create UNO Deck
colors = ["Red", "Green", "Blue", "Yellow"]
numbers = [str(i) for i in range(10)]

deck = [(c, n) for c in colors for n in numbers]
random.shuffle(deck)

# Deal cards
player_hand = [deck.pop() for _ in range(7)]
computer_hand = [deck.pop() for _ in range(7)]

top_card = deck.pop()

# Check valid move
def valid_move(card):
    return card[0] == top_card[0] or card[1] == top_card[1]

# Play card
def play_card(index):
    global top_card

    card = player_hand[index]

    if valid_move(card):
        top_card = card
        player_hand.pop(index)

        if len(player_hand) == 0:
            status.config(text="🎉 You Win!")
            return

        computer_turn()
        update_ui()
    else:
        status.config(text="Invalid Move!")

# Computer Turn
def computer_turn():
    global top_card

    for card in computer_hand:
        if valid_move(card):
            top_card = card
            computer_hand.remove(card)

            if len(computer_hand) == 0:
                status.config(text="💻 Computer Wins!")
            return

    if deck:
        computer_hand.append(deck.pop())

# Update UI
def update_ui():
    top_label.config(text=f"Top Card: {top_card[0]} {top_card[1]}")

    for widget in cards_frame.winfo_children():
        widget.destroy()

    for i, card in enumerate(player_hand):
        btn = tk.Button(
            cards_frame,
            text=f"{card[0]} {card[1]}",
            command=lambda i=i: play_card(i)
        )
        btn.pack(side=tk.LEFT, padx=5)

# GUI
root = tk.Tk()
root.title("UNO Game")

top_label = tk.Label(root, font=("Arial", 16))
top_label.pack(pady=10)

cards_frame = tk.Frame(root)
cards_frame.pack(pady=20)

status = tk.Label(root, text="Your Turn", fg="blue")
status.pack()

update_ui()

root.mainloop()