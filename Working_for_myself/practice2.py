#---Author: Laura Linares---
#--------Version: V1--------
#----Script: Practice 2-----
#-- Use: changes a personal email to a company email

#--Library importation--
import time
import os

#--Variable declaration--
newEmailsFile='new_emails.txt'

#--Function declaration--
def clean():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def ChangeEmail(routefile,lastPartofEmail):
    #-----Read the file------
    with open(routefile,"r") as f, open(newEmailsFile, "a") as new_f:
        for line in f:
            # Separate the line in two parts [NameLastName 0] [email 1]
            newline=line.strip().split(':')
            # A new variable that will have the value of the email section
            email=newline[1].strip()
            # Separate the personal ending spliting the email into two sections
            emailpart=email.split('@')
            # Create the new email with the first part and the second part gived by the user
            newEmail=f"{emailpart[0]}@{lastPartofEmail}"
            # Write the new employee with email in the new file
            new_f.write(f"{newline[0]}:{newEmail}\n")

#------Script starts-----
clean()

# Data recolect
print("Hello, user. This is an AUTOMATIZED program that changes your employees personal e-mails to company e-mails \n")
time.sleep(2)
print("Please, introduce the route of the file that contains the emails in this format...: \n")
print("Name,LastName:personalemail@example.com \n")
input_file=input("Route: ")
print("\n")

#-Cheking Errors on File-
if not os.path.exists(input_file):
    print("Error. Your route is not correct. It doesn't exists \n")
    print("Exiting...")
    exit(1)
if not os.path.isfile(input_file):
    print("Error. The route you specified is not a file \n")
    print("Exiting...")
    exit(1)
if not os.path.exists(newEmailsFile):
    with open(newEmailsFile, 'w') as f:
        pass

# More data recolect
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

clean()
print("Working on the file... \n")
time.sleep(2)
ChangeEmail(input_file,lastPartofEmail)

print("The changes have been done \n")
print("Thank you for using this script \n")
print("Have a nice day!")
exit(0)