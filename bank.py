import os
from view_records import list_all_customers, list_transactions_for_customer, list_accounts_for_customer
from add_records import (
    add_customer_to_db, add_account_to_db, customer_exists,
    add_transaction_to_db, account_exists,
    get_customer_id_and_balance_for_account, update_account_balance
)
from lib.dbfolder.delete_customer import delete_customer_and_associated_data
from datetime import datetime

# ANSI color codes for text formatting
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
def clear_screen():
    os.system('clear')  # Replace with 'cls' for Windows

def print_header(text):
    
    print(GREEN + f"=== {text} ===" + RESET)

def print_success(message):
    print(GREEN + message + RESET)

def print_error(message):
    print(RED + message + RESET)

# Rest of the code remains the same...


def main():
    while True:
        print_header("Bank Management System")
        print("Options:")
        print("1. Press 'S' to see records.")
        print("2. Press 'F' to add new records")
        print("3. Press 'R' to delete customer and associated data.")
        print("4. Press 'Q' to quit.")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 's':
            view_records_menu()
        elif choice == 'f':
            add_records_menu()
        elif choice == 'r':
            delete_customer()
        elif choice == 'q':
            print_success("Exiting the program.")
            break
        else:
            print_error("Invalid choice. Please try again.")

def view_records_menu():
    while True:
        print_header("View Records Menu")
        print("1. Press 'C' to see all customers.")
        print("2. Press 'T' to see transaction records for a specific customer.")
        print("3. Press 'A' to see account records for a specific customer.")
        print("4. Press 'B' to go back to the main menu.")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'c':
            list_all_customers()
        elif choice == 't':
            transaction_records() 
        elif choice == 'a':
            account_records()       
        elif choice == 'b':
            break
        else:
            print_error("Invalid choice. Please try again.")

def transaction_records():
    print_header("View Transactions for a Customer")
    customer_id = input("Enter the ID of the customer: ").strip()

    if customer_id:
        try:
            customer_id = int(customer_id)
            list_transactions_for_customer(customer_id)
           
        except ValueError:
            print_error("Invalid customer ID. Please enter a valid ID.")

def account_records():
    print_header("View Accounts for a Customer")
    customer_id = input("Enter the ID of the customer: ").strip()

    if customer_id:
        try:
            customer_id = int(customer_id)
            list_accounts_for_customer(customer_id)
           
        except ValueError:
            print_error("Invalid customer ID. Please enter a valid ID.")

def add_records_menu(): 
    clear_screen()
    while True:
        print_header("Add Records Menu")
        print("1. Press 'C' to add a new customer.")
        print("2. Press 'T' to add a new transaction.")
        print("3. Press 'A' to add a new account.")
        print("4. Press 'B' to go back to the main menu.")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'c':
            add_customer()
        elif choice == 't':
            add_transaction()
        elif choice == 'a':
            add_account()       
        elif choice == 'b':
            break
        else:
            print_error("Invalid choice. Please try again.")

def add_customer():
    print_header("Add a New Customer")
    first_name = input("Enter the first name of the customer: ").strip()
    last_name = input("Enter the last name of the customer: ").strip()
    
    if first_name.isalpha() and last_name.isalpha():
        customer_id = add_customer_to_db(first_name, last_name)
        print_success(f"Customer {first_name} {last_name} has been added to the database.")
        print(f"Customer ID: {customer_id.id}")
    else:
        print_error("Invalid input. Please enter valid first and last names with alphabetic characters.")

def add_account():
    print_header("Add a New Account")
    
    # Prompt for account type (savings or current)
    while True:
        account_type = input("Enter the account type (savings or current): ").strip().lower()
        if account_type not in ["savings", "current"]:
            print_error("Invalid account type. Please enter 'savings' or 'current'.")
        else:
            break
      
    # Prompt for account balance
    while True:
        account_balance_str = input("Enter the initial deposit: ").strip()
        try: 
            account_balance = float(account_balance_str)
            if account_balance < 0:
                print_error("Invalid input. Please enter a positive number for account balance.")
            else:
                break
        except  ValueError: 
            print_error("Invalid input. Please enter a positive number for account balance.")        
        
    # Prompt for customer ID
    while True:
        customer_id_str = input("Enter the ID of the customer: ").strip()
        try:
            customer_id = int(customer_id_str)
            if not (customer_id > 0 and customer_exists(customer_id)):
                print_error("Customer not in database.")
            else:
                break
        except ValueError:
            print_error("Invalid input. Please enter a positive number for customer ID.")
    
    # Call the add_account_to_db function with the validated parameters
    new_account = add_account_to_db(account_type, account_balance, customer_id)

    if new_account:
        print_success(f"Account for customer {customer_id} has been added to the database.")
        print(f"Account ID: {new_account.id}")

def add_transaction():
    print_header("Add a New Transaction")
    
    # Prompt for account ID
    while True:
        account_id_str = input("Enter the ID of the account: ").strip()
        try:
            account_id = int(account_id_str)
            if not (account_id > 0 and account_exists(account_id)):
                print_error("Account not in the database.")
            else:
                # Retrieve the customer ID and current account balance associated with the account
                customer_id, current_balance = get_customer_id_and_balance_for_account(account_id)
                if customer_id is not None:
                    break
                else:
                    print_error("Customer ID not found for the account.")
        except ValueError:
            print_error("Invalid input. Please enter a positive number for account ID.")
    
    # Prompt for amount
    while True:
        amount_str = input("Enter the amount: ").strip()
        try:
            amount = float(amount_str)
            if amount < 0:
                print_error("Invalid input. Please enter a positive number for the amount.")
            else:
                break
        except ValueError:
            print_error("Invalid input. Please enter a positive number for the amount.")
    
    while True:
        description = input("Enter the transaction description (deposit or withdrawal): ").strip().lower()
        if description not in ["deposit", "withdrawal"]:
            print_error("Invalid account type. Please enter 'deposit' or 'withdrawal'.")
        else:
            break
    
    date = datetime.now().date()
    
    # Determine if the transaction is a deposit or withdrawal and update the account balance accordingly
    if description == "deposit":
        new_balance = current_balance + amount
    else:
        new_balance = current_balance - amount
    
    # Call the add_transaction_to_db function with the validated parameters
    new_transaction = add_transaction_to_db(date, description, amount, customer_id, account_id)

    if new_transaction:
        # Update the account balance in the database
        update_account_balance(account_id, new_balance)
        
        print_success(f"Transaction for customer {customer_id} and account {account_id} has been added to the database.")
        print(f"Transaction ID: {new_transaction.id}")
        print(f"Updated Account Balance: {new_balance}")
def delete_customer():
    clear_screen()
    print_header("Delete a customer:")
    
    # Prompt for customer ID
    while True:
        customer_id_str = input("Enter the ID of the customer: ").strip()
       
        try:
            customer_id = int(customer_id_str)
                  
            if not (customer_id > 0 and customer_exists(customer_id)):
                print_error("Customer not in the database.")
            else:
                break  
        except ValueError:
            print_error("Invalid input. Please enter a positive number for customer ID.")
    
    # Call the delete_customer_and_associated_data function with the validated parameters
    delete_customer_and_associated_data(customer_id)
    
    print_success(f"Customer with ID {customer_id}, associated accounts, and transactions have been deleted.")   

if __name__ == "__main__":
    main()