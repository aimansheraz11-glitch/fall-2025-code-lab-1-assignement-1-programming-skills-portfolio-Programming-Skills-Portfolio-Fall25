"""
a = 30
while (a==30): 
 print ("You are in loop")
 break


#fruits = ["apple", "banana", "cherry"]
for i in range(2):
  print(i)
"""
menu = ["chicken", "cheese","bbq" , "beef" ]
while True:
    order = input("What kind of sandwich would you like? ")
    if order in menu:
        print(f"Here is your {order} sandwich")
    else:
        print("Sorry we don't have that")
    break
    