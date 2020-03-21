import os
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
int(ch)
print(ch)

