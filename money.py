bank = 0
withdraw=0

while(True) :
    question1 = input("What would you like to do? Enter d for depositing, w for withdrawing, b for balence, and s for subtracting money: ")
    if question1 == "d":
        
        deposit = float(input("Please enter how much you would like to deposit: "))
        bank = bank+deposit
        print("Succesfully deposited!")
    elif question1 == "w":
        withdraw = float(input("Please enter how much you would like to withdraw to buy something: "))
        if bank-withdraw>=0:
            print("Succesfully Withdrew!")
            bank=bank-withdraw
        else:
            print("You do not have that much money in your bank!")
    elif question1 == "b":
        print("You have ",bank," dollars deposited and ",withdraw," dollars in your pocket")
    elif question1 == "s":
        item = input("What are you buying today?: ")
        cost = float(input("How much does this cost?: "))
        if withdraw-cost>=0:
            print("Successfully bought "+item+"!")
            withdraw=withdraw-cost
        else:
            print("You do not have that much money in your pocket! Withdraw some more from the bank.")
    else:
        print("ERROR")
    print("Amount in bank: ",bank)
    print("Ammount in wallet: ",withdraw)
    

