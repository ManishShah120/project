import os
import sys
os.system("tput setaf 1")
print("\t\t\t\t\t-:Hey wellcome to my TUI that makes life simple:-")
os.system("tput setaf 7")
print("\t\t\t\t\t-------------------------------------------------")

print("""
        Press 1: DATE
        Press 2: CALENDAR
        Press 3: CONFIGURE WEB SERVER
        Press 4: CREATE USER
        Press 5: CREATE FILE
        Press 6: SETUP NETWORKING
        Press 7: EXIT
""")

ch = input("Enter your CHOICE: ")
ch = int(ch)
if ch == 1:
	os.system("date")
elif ch == 2:
	os.system("cal")
elif ch == 3:
	print("Configuring web server...")
	os.system("sudo apt install apache2")
elif ch == 4:
	create_user = input("User Name: ")
	os.system("sudo useradd {}".format(create_user))
	print("creating User...")
	print("Do you want to set the password for ",create_user," now:(y/n)")
	y_n = input()
	if y_n == 'y':
		os.system("passwd {}".format(create_user))
	else:
		exit()
elif ch == 5:
	file_name = input("Enter the file name with extension: ")
	os.system("gedit {}".format(file_name))
	print("Creating ",file_name," ...")
elif ch == 6:
	printf("Setting up Network...")
elif ch == 7:
	exit()
else:
	print("Please Enter a valid choice...")
	os.system("exit")
