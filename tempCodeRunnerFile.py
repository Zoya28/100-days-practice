
print(logo)
print("Welcome to the secret auction program!")
it_continues = True
record={}
def high_bid(record):
  highest_bid=0
  winner=""
  for key in record:
    if record[key]> highest_bid:
      highest_bid=record[key]
      winner=key
  print(f"The winner is {winner} with the highest bid of ${highest_bid}")

while it_continues:
  name = input("Whai is your name?  ")
  bid = int(input("What is your Bid?  "))
  record[name] = bid
  new_bidder=input("Are there any other bidders? Type 'yes' or 'no'\n")
  if new_bidder=="yes":
    os.system("cls")
  else:
    it_continues = False

high_bid(record)
