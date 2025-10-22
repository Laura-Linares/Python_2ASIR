#---Author: Laura Linares---
#--------Version: V1--------
#----Script: Practice 1-----

#--Variable declaration--
username='laura'
password='1234root'
#--Function declaration--
def welcome():
    print(f"Welcome, {name}. Now you are logged in")

#------Script starts-----
import os
os.system("cls")

name=input("Please, introduce your user name: ").lower()

if name == username:
    passw=input("Please, introduce your password: ")

    if passw == password:
        welcome()
    else:
        tries=2
        while tries > 0 and passw != password:
            print("")
            print("Your password is incorrect. Try again.")
            print("")
            print(f"You have {tries} tries left")
            print("")
            passw=input("Please, introduce your password: ")
            tries-=1
            if tries == 0:
                print("Sorry, you have no more tries")
                print("Exiting...")
            if passw == password:
                welcome()
else:
    print("Your username is not correct")
    print("Exiting...")    