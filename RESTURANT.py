# Define the menu of restaurant using dictionary 
menu={
    'Pizza':40,
    'Pasta':30,
    'Cheeseburger':34,
    'Cheese sandwich':55,
    'Corn dog':70,
    'Cold Coffee':90,
    'Mojito':70,
}

print('WELCOME TO OUR RESTAURANT')
print("\nMENU")
print("\nPizza : RS.40\nPasta : RS. 30\nCheeseburger : RS. 34\nCheese sandwich : RS. 55\nCorn dog : RS. 70\nCold Coffee : RS. 90\nMojito : RS. 70\n")

Ordertotal=0

item1=input("\nEnter the dish:- \n")
if item1 in menu:
    Ordertotal += menu[item1]
else:
    print("Order item ",item1,"is not avaialable.")
    
anotherorder=input("Do you want to order another item? (YES/NO)")
if anotherorder == "YES":
    item2 = input("Enrer your order.")
    if item2 in menu:
        Ordertotal += menu[item2]
    else:
        print("Order item ",item2," is not avaialable.")
        
print("Total amount is ", item1+ item2, Ordertotal)