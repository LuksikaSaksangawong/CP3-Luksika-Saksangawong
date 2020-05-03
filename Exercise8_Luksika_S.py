UserName = input("Username :")
PassWord = input("Password :")
CakePrice = 45
CupcakePrice = 35
MacaronPrice = 35
if UserName == "Admin" and PassWord == "12345":
    print("Welcome to Sweet shop")
    print("---------menu---------")
    print("1.Cake     45 ฿")
    print("2.Cupcake  35 ฿")
    print("3.Macaron  35 ฿")
    print("----------------------")
    Sweet = int(input("Please select menu :"))
    if Sweet == 1:
        print("Cake")
        Number = int(input("How many Pieces do you want ? :"))
        print("Total price is",CakePrice*Number,"฿.")
    elif Sweet == 2:
        print("Cupcake")
        Number = int(input("How many Pieces do you want ? :"))
        print("Total price is", CupcakePrice * Number, "฿.")
    elif Sweet == 3:
        print("Macaron")
        Number = int(input("How many Pieces do you want ? :"))
        print("Total price is", MacaronPrice * Number, "฿.")
    else:
        print("Wrong input")
else:
    print("Error")
