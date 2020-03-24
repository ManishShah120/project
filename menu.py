import os
import sys
os.system("tput setaf 1")
print("\t-:Hey wellcome to my TUI that makes life simple:-")
os.system("tput setaf 7")
print("\t-------------------------------------------------")
os.system("tput setaf 2")
print("""
	Press 1: DATE
	Press 2: CALENDAR
	Press 3: CONFIGURE WEB SERVER
	Press 4: CREATE USER
	Press 5: CREATE FILE
	Press 6: SETUP NETWORKING
	Press 7: EXIT
""")
os.system("tput setaf 7")
#********************local*******************************
def programlocal():
	while True:
		os.system("tput setaf 2")
		print("""
		Press 1: DATE
		Press 2: CALENDAR
		Press 3: CONFIGURE WEB SERVER
		Press 4: CREATE USER
		Press 5: CREATE FILE
		Press 6: SETUP NETWORKING
		Press 7: EXIT
		""")
		os.system("tput setaf 7")
		ch = input("Enter your CHOICE: ")
		ch = int(ch)
		os.system("tput setaf 3")
		if ch == 1:
			os.system("date")
		elif ch == 2:
			os.system("cal 2020")
		elif ch == 3:
			print("Configuring web server...")
			os.system("yum install httpd")
		elif ch == 4:
			create_user = input("User Name: ")
			os.system("useradd {}".format(create_user))#This curly braces is known as Place Holder; An ddot format is a string function
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
			print("Setting up Network...")
		elif ch == 7:
			print("Thanks for using this service EXITING...")
			os.system("tput setaf 7")
			exit()
		else:
			print("Please Enter a valid choice...")
		os.system("tput setaf 7")

#*******************************************remote***************************************
def programremote(remoteIP):
	while True:
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
			os.system("ssh {} date".format(remoteIP))
		elif ch == 2:
			os.system("ssh {} cal 2020".format(remoteIP))
		elif ch == 3:
			print("Configuring web server...")
			os.system("ssh {} yum install httpd".format(remoteIP))
		elif ch == 4:
			create_user = input("User Name: ")
			os.system("ssh {} useradd {}".format(remoteIP, create_user))#This curly braces is known as Place Holder; An ddot format is a string function
			print("creating User...")
			print("Do you want to set the password for ",create_user," now:(y/n)")
			y_n = input()
			if y_n == 'y':
				os.system("ssh {} passwd {}".format(remoteIP, create_user))
			else:
				exit()
		elif ch == 5:
			file_name = input("Enter the file name with extension: ")
			os.system("ssh {} gedit {}".format(remoteIP, file_name))
			print("Creating ",file_name," ...")
		elif ch == 6:
			print("Setting up Network...")
		elif ch == 7:
			print("Thanks for using this service EXITING...")
			exit()
		else:
			print("Please Enter a valid choice...")

#************************************Driver****************************
location = input("Where would you like to perform job (local/remote): ")
if (location == 'local'):
		programlocal()
elif (location == 'remote'):
		remoteIP = input("Enter your IP: ")
		programremote(remoteIP)
else:
	print("You have not selected the correct choice")
	os.system("tput setaf 1")
	print("EXITING...")
	os.system("tput setaf 7")
