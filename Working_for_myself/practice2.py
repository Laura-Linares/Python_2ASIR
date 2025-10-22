#---Author: Laura Linares---
#--------Version: V1--------
#----Script: Practice 2-----

#--Variable declaration--

#--Function declaration--

#------Script starts-----
import os
import time
os.system("cls")

print("Hello, user. This is an AUTOMATIZED program that changes your employees personal e-mails to company e-mails")
time.sleep(2)
print("")
print("Please, introduce the route of the file that contains the emails in this format...:")
print("")
print("Name,LastName-personalemail@example.com")
file=input("Route: ")

#------Error control-----


#-----Read the file------
with open(file,"r") as f:
    for line in f:
        