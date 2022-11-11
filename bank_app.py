#!/bin/python3
 # 1. using the import module
# 2. understanding lists
# 3. understanding loops
# 4. understanding switch

print("Welcome to International banking app \nWhere your comfort is our priority") # The "\n" is for a new line

password = 7777
user_choice = 0
balance = 1000
know_your_customer = []

pin = int(input("Enter your 4 digit pin to login: \n"))

if pin == password:
  while user_choice != 5:
    print("\n\n**********MENU*************")
    print("1) Balance")
    print("2) Deposit")
    print("3) Withdrawal")
    print("4) Create New Account")
    print("5) Quit Anyway \n")

    user_choice = int(input("Enter your choice: \n"))
    if user_choice == 1:
            print("Your balance is "+ str(balance)) # Converting the balance from int to str
    elif user_choice == 2:
            deposit = int(input("Enter Amount"))
            balance += deposit # This means balance is = balance + deposit
            print(" \n ")

    elif user_choice == 3:
      withdraw = int(input("How much do you want to withdraw: "))
      balance -= withdraw
      print(" \n You just withdrawed" + str(withdraw) + "naira")
      print("Your balance is now: " + str(balance)) 

    elif user_choice == 4: 
      new_account_name = input("\n Enter your name: ")
      know_your_customer.append(new_account_name)
      address = input("\n Enter your address in full: ")
      know_your_customer.append(address)
      phone_number = input("\n Enter your phone number: ")
      know_your_customer.append(phone_number)
      bvn = input("\n Enter your bvn details: ")
      know_your_customer.append(bvn)

      for each_detail in know_your_customer:
        print(each_detail)

      print(know_your_customer)

    elif user_choice == 5:
      
      print("Goodbye!")
      break

else:
  print("Pin is incorrect, please try next time...")
