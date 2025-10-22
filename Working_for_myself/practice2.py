#---Author: Laura Linares---
#--------Version: V1--------
#----Script: Practice 2-----
#-- Use: changes a personal email to a company email

#--Variable declaration--
newEmailsFile='new_emails.txt'

#--Function declaration--
def ChangeEmail():
    #-----Read the file------
    with open(file,"r") as f:
        for line in f:
            # Separate the line in two parts [NameLastName 0] [email 1]
            newline=line.split(':')
            # A new variable has the value of the email section
            email=line[1]
            # Find the @ to separate the personal ending
            separation=email.find('@')
            # Create the new email with the first part and the second part gived by the user
            newEmail=email[:separation] + lastPartofEmail
            # Write the new employee with email in a new file
            with open(newEmailsFile, 'a') as f:
                f.write(f"{newline[0]}:{newEmail}\n")


#------Script starts-----
import os
import time
os.system("cls")

# Data recolect
print("Hello, user. This is an AUTOMATIZED program that changes your employees personal e-mails to company e-mails \n")
time.sleep(2)
print("Please, introduce the route of the file that contains the emails in this format...: \n")
print("Name,LastName:personalemail@example.com \n")
file=input("Route: ")
print("\n")

lastPartofEmail=input("Please, now introduce your company extension 'g.e. example.com': ")
print("")
answer=input(f"Your company extension is {lastPartofEmail}? (yes/no): ").lower()
while answer != 'yes' and answer != 'y' and answer != '*':
    if answer == 'no' or answer == 'n':
        print("It's okay! You can type it again! \n")
        while (answer != 'yes' or answer != 'y') and answer != '*':
            lastPartofEmail=input("Please, now introduce your company extension 'g.e. example.com': ")
            print("\n")
            print("You can exit this program if you are not sure about something typing '*' \n")
            answer=input(f"Your company extension is {lastPartofEmail}? (yes/no): ").lower()
    else:
        print("You typed something different \n")
        print("Coming back to the question so you can answer it again! \n")
        print("Also, you can exit typing '*' \n")
    answer=input(f"Your company extension is {lastPartofEmail}? (yes/no): ").lower()

print("you said yes! :)")

#-Cheking Errors on File-