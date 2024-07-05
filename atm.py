# setting the atm menu 
Balance = 1000
print("a.Checking Balance")
print("b.Depositing Money")
print("c.withdraw MOney")
print("d.exit")

#prompting the user to choose from list options
choice = input("choose your options here:")
if choice == "a":
    print("Balance: is:{Balance}")
elif choice == "b":
     
    deposit =(input("enter amount to deposit:"))
    Balance = Balance + deposit
    print(f"{deposit} the new balance is: {Balance}")
elif choice == "c":
    
    withdraw = (input(f"enter amount to withdraw"))
    if withdraw <= Balance:
        Balance = Balance - withdraw
        print(f"{withdraw} withdraw.new balance and {Balance}")
    elif choice == "d":
        print("no moneny availble ")
        
    else:
        print("invalid choice")

    
   




    
    

    











    