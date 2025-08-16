"""import logging as lg
lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format = "[%(asctime)s-%(levelname)s]-%(message)s"
)
account_table={12345:6789}

def valid_user(account_number,pin):
    lg.debug("user in login page")
    if account_number in account_table:
        if account_table[account_number]==pin:
            lg.info("user successfully logged in")
            return True
        else:
            lg.warning("please check your login credentials")
            return False
    else:
        lg.warning("please check your login credentials")
        print("please check your credentials")
        return False

if __name__=="__main__":
    print("welcome to python class")
    lg.info("welcome to python class")
    account_number=int(input("please enter accout number:"))
    pin=int(input("please enter pin number"))
    if valid_user(12345,125):
        pass"""
import logging as lg
lg.basicConfig(
    filename="app.py",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)
# total Operations
operations = (
    "1. Balance\n",
    "2. withdraw\n",
    "3. deposite\n",
    "4. Transfer\n",
    "5. History\n",
    "6.exit\n"
)
# account table 
account_table = {
    12345:6789,
    123456:6789
    }
# useres tables
users_table = {
    12345:["Akshaya", "giramgariakshaya@gmail.com", 1000],
    123456:["Aks", "gmail@.com", 2500]}
# transcations table 

# Checking valid user
def valid_user(user_name:int, password:int):
    lg.debug("User in login page")
    if user_name in account_table:
        if account_table[user_name] == password:
            lg.info("User successfully logined")
            print("User successfully logined")
            return True
        else:
            lg.warning("Please check your login credentials")
            print("Please check your login credentials")
            return False
    else:
        lg.warning("Please check check your login credentials")
        print("Please check check your login credentials")
        return False
    
# balence function
def balence(user_name:int):
    lg.debug("User in balence page")
    if user_name in users_table:
        amount = users_table[user_name][2]
        lg.info(f"{user_name} user current balence is {amount}")
        print(f"{user_name} user current balence is {amount}")
    else:
        lg.warning("User not found")
        print("User not found")
    

# withdraw function
def withdraw(user_name):
    lg.debug("User in withdraw page")
    amount = users_table[user_name][2]
    withdraw_amount = int(input("Please enter withdraw amount: "))
    if amount >= withdraw_amount:
        users_table[user_name][2] -= withdraw_amount
        lg.info(f'{withdraw_amount} withdraw successful and current balence is {users_table[user_name][2]}')
        print(f'{withdraw_amount} withdraw successful and current balence is {users_table[user_name][2]}')

    else:
        lg.warning("Insufficent amount")
        print("Insufficent amount")
    

# deposite function
def deposite(user_name:int):
    lg.debug("User in deposite page")
    deposite_amount = int(input("Please enter deposite amount: "))
    if user_name in users_table:
        users_table[user_name][2] += deposite_amount
        lg.info(f'{deposite_amount} deposite successful and current balence is {users_table[user_name][2]}')
        print(f'{deposite_amount} deposite successful and current balence is {users_table[user_name][2]}')

    else:
        lg.warning("User not found")
        print("User not found")
    

# transer function
def transfer(user_name):
    lg.debug("User in transfer page")
    recevier_account = int(input("Enter Recevier account number: "))
    amount = int(input("Enter amount: "))
    lg.info(f"recevier account is {recevier_account} and amount is {amount}")
    current_amount = users_table[user_name][2]
    if recevier_account in users_table:
        if current_amount >= amount:
            # amount updatetion in users table
            users_table[user_name][2] -= amount
            users_table[recevier_account][2] += amount
            lg.info(f'{amount} transfer successfully and current balence is {users_table[user_name][2]}')
            print(f'{amount} transfer successfully and current balence is {users_table[user_name][2]}')
            
        else:
            lg.warning("Insufficent amount")
            print("Insufficent amount")
    else:
        lg.warning(f'{recevier_account} not found')
        print(f'{recevier_account} not found')

# history function
def history(user_name):
    lg.info("User in history page")
    print("History function under development process....")
    

# exit function
def exit_fun():
    lg.info("User in exit page")
    print("Successfully exited, thankyou for using codegnan online bank services")
    return True
    

# chose_operation function
def chose_operation(account_no, choice):
    lg.info(f"selected operation is {operations[choice-1]}")
    val = False
    if choice == 1:
        balence(user_name=account_no)
    elif choice == 2:
        withdraw(user_name= account_no)
    elif choice == 3:
        deposite(user_name= account_no)
    elif choice == 4:
        transfer(user_name= account_no)
    elif choice == 5:
        history(user_name= account_no)
    elif choice == 6:
        val = exit_fun()
    else:
        print("Please selct between 1-6")
    if val:
        return val

if __name__ == "__main__":
    print("Welcome to the online codegnan Banking")
    lg.info("Welcome to the online codegnan Banking")
    account_no = int(input("Please, enter account number: "))
    pin =int(input("Please enter pin number: "))
    lg.info(f"User credenctials are {account_no} and {pin}")
    while True:
        if valid_user(user_name=account_no,password=pin):
            print(*operations)
            lg.info(operations)
            choice = int(input("Please select operation (1-6): "))
            exit_fun_val = chose_operation(account_no=account_no, choice=choice)
            if exit_fun_val:
                break
        else:
            lg.warning("User not found, please check with your login credentials")
            print("User not found, please check with your login credentials")
            break[2025-08-16 14:58:46,211 - INFO] - Welcome to the online codegnan Banking
