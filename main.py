from replit import clear
from art import logo
#You can call clear() to clear the output in the console.
print(logo)
mode = True
auction = {}

def winner(bids):
  highiest_bid = 0
  winner_name = ""
  for bidder_name in bids:
    amount = bids[bidder_name]
    if amount > highiest_bid:
      highiest_bid = amount
      winner_name = bidder_name
  print(f"The winnder of the auction is {winner_name} with a bid of ${highiest_bid}.")
  

while mode:
  name = input("What is your name? ")
  bid = int(input("What is your bid?: $"))
  auction[name] = bid
  contin = input("Are there any other bidders? Type 'yes' or Type 'no'. ")
  if contin == "no":
    mode = False
    winner(auction)
  elif contin == "yes":
    clear()
  
