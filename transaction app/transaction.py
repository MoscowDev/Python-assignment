def get_deposit(amount, balance=0, transactions=None):
    if transactions is None:
        transactions = []
    balance += amount
    transactions.append(f"Deposited ₦{amount}, new balance ₦{balance}")
    return balance


def get_withdrawal_balance(amount, balance=0, transactions=None):
    if transactions is None:
        transactions = []
    if amount > balance:
        print("Insufficient balance.")
        return balance, transactions
    balance -= amount
    transactions.append(f"Withdrew ₦{amount}, new balance ₦{balance}")
    return balance, transactions


def show_transactions(transactions):
    if not transactions:
        print("No transactions yet.")
    else:
        for count in transactions:
            print(count)
