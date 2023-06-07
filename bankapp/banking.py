# created by Toby Cantello
# created on 6/5/2023
# last updated on 6/6/23

# Imports
import sqlite3

# Connection to database
try:
    sqliteConnection = sqlite3.connect('bankDB.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

# Funtions
def Balance():
   print('This is inside Balance Function')

def Withdraw():
    print('This is inside Withdrawn Function')

def Deposit():
    print('This is inside Deposit Function')

# start of the program
print ('Welcome to Cantello Bank')
print ('')
user_input = input('please enter your email address: ')
print('')
print (user_input, 'how can we help you today?')
customer_choice = int(input(' 1 for Account Balance\n 2 for Withdraw\n 3 for Deposit\n What is your choice? '))
if customer_choice == 1:
    Balance()
elif customer_choice == 2:
    Withdraw()
elif customer_choice == 3:
    Deposit()
