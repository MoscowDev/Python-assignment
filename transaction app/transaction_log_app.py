from transaction import *

menu = """
WELCOME TO TRANSACTION LOG App

1 -> Deposit
2 -> Withdrawal
3 -> Show Transactions
4 -> Exit
"""

print(menu)

account_balance = 0
transactions = []
user = ""

while user != "4":
    user = input("Enter choice: ")

    match user:
        case "1":
            deposit = float(input("Enter the amount you want to deposit: "))
            account_balance, transactions = get_deposit(deposit, account_balance, transactions)
            print(f"Deposited ₦{deposit}, new balance ₦{account_balance}")

        case "2":
            withdraw_amount = float(input("Enter the amount you want to withdraw: "))
            account_balance, transactions = get_withdrawal_balance(withdraw_amount, account_balance, transactions)
            print(f"Withdrew ₦{withdraw_amount}, new balance ₦{account_balance}")

        case "3":
            print("\nTransaction History:")
            show_transactions(transactions)
            print()

        case "4":
            print("Thank you for using Transaction Log App!")
            break

        case _:
            print("Invalid option. Please try again.")
