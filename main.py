import sys

print("Hi, lets list an item for auction!")
Item_name = input("Enter the item name: ")

Item_price = float(input("Enter the item price: "))
if Item_price <= 0:
    print("Please enter a valid number more than 0.")
    sys.exit()
  
while True:
    ans = (input("would you like to place a bidding?(yes/no):"))    
    if ans =="no":
      print("okay, lets place a bid another time!")
      sys.exit()
    else:
        print("okay, place a bid!")
               
    bid = float(input("Enter the bid amount: "))
     
    if bid <= 0:
        print("Please enter a valid number more than 0.")
        sys.exit()
  
    if bid < Item_price:
     print(f"Sorry, You did not win the auction for {Item_name}. The highest bid was ${Item_price: .2f}")
    
     
      
    else:
      print(f"Congragulations! you won the auction for {Item_name} with a price of ${Item_price: .2f}")
  
      break
  
  
  



 
  
