def buy_petrol(option, transaction=None):
    if transaction is None:
        transaction = []

    option = input("Choose 'amount' or 'litre': ").lower()
    receipt = ""

    if option == "amount":
        petrol_amount = int(input("Enter amount for Petrol: "))
        litre = petrol_amount // 650
        receipt = f"""
        Customers Transaction Receipt
        ==================================
        = Product: Petrol               =
        = Amount: {petrol_amount} NGN   =
        = Liters: {litre} L             =
        = Thank you For your Patronage  =
        ==================================
        Saving Transaction History...
        """
        print(receipt)
        transaction.append(receipt)

    elif option == "litre":
        litre_quantity = int(input("Enter quantity in litres: "))
        petrol_amount = litre_quantity * 650
        receipt = f"""
        Customers Transaction Receipt
        ==================================
        = Product: Petrol               =
        = Amount: {petrol_amount} NGN   =
        = Liters: {litre_quantity} L    =
        = Thank you For your Patronage  =
        ==================================
        Saving Transaction History...
        """
        print(receipt)
        transaction.append(receipt)

    else:
        print("Invalid option. Choose 'amount' or 'litre'.")
    return transaction


def get_diesel(option, transaction=[]):
    #if transaction is None:
       # transaction = []

    option = input("Choose 'amount' or 'litre': ").lower()
    receipt = ""

    if option == "amount":
        diesel_amount = int(input("Enter amount for Diesel: "))
        litre = diesel_amount // 720
        receipt = f"""
        Customers Transaction Receipt
        ==================================
        = Product: Diesel               =
        = Amount: {diesel_amount} NGN   =
        = Liters: {litre} L             =
        = Thank you For your Patronage  =
        ==================================
        Saving Transaction History...
        """
        print(receipt)
        transaction.append(receipt)

    elif option == "litre":
        litre_quantity = int(input("Enter quantity in litres: "))
        diesel_amount = litre_quantity * 720
        receipt = f"""
        Customers Transaction Receipt
        ==================================
        = Product: Diesel               =
        = Amount: {diesel_amount} NGN   =
        = Liters: {litre_quantity} L    =
        = Thank you For your Patronage  =
        ==================================
        Saving Transaction History...
        """
        print(receipt)
        transaction.append(receipt)

    else:
        print("Invalid option. Choose 'amount' or 'litre'.")
    return transaction


def get_kerosene(option, transaction=None):
    if transaction is None:
        transaction = []

    option = input("Choose 'amount' or 'litre': ").lower()
    receipt = ""

    if option == "amount":
        kerosene_amount = int(input("Enter amount for Kerosene: "))
        litre = kerosene_amount // 550
        receipt = f"""
        Customers Transaction Receipt
        ==================================
        = Product: Kerosene             =
        = Amount: {kerosene_amount} NGN =
        = Liters: {litre} L             =
        = Thank you For your Patronage  =
        ==================================
        Saving Transaction History...
        """
        print(receipt)
        transaction.append(receipt)

    elif option == "litre":
        litre_quantity = int(input("Enter quantity in litres: "))
        kerosene_amount = litre_quantity * 550
        receipt = f"""
        Customers Transaction Receipt
        ==================================
        = Product: Kerosene             =
        = Amount: {kerosene_amount} NGN =
        = Liters: {litre_quantity} L    =
        = Thank you For your Patronage  =
        ==================================
        Saving Transaction History...
        """
        print(receipt)
        transaction.append(receipt)

    else:
        print("Invalid option. Choose 'amount' or 'litre'.")
    return transaction


def get_gas(option, transaction=None):
    if transaction is None:
        transaction = []

    option = input("Choose 'amount' or 'litre': ").lower()
    receipt = ""

    if option == "amount":
        gas_amount = int(input("Enter amount for Gas: "))
        litre = gas_amount // 480
        receipt = f"""
        Customers Transaction Receipt
        ==================================
        = Product: Gas                  =
        = Amount: {gas_amount} NGN      =
        = Liters: {litre} L             =
        = Thank you For your Patronage  =
        ==================================
        Saving Transaction History...
        """
        print(receipt)
        transaction.append(receipt)

    elif option == "litre":
        litre_quantity = int(input("Enter quantity in litres: "))
        gas_amount = litre_quantity * 480
        receipt = f"""
        Customers Transaction Receipt
        ==================================
        = Product: Gas                  =
        = Amount: {gas_amount} NGN      =
        = Liters: {litre_quantity} L    =
        = Thank you For your Patronage  =
        ==================================
        Saving Transaction History...
        """
        print(receipt)
        transaction.append(receipt)

    else:
        print("Invalid option. Choose 'amount' or 'litre'.")
    return transaction


def get_transaction_history(transaction=None):
    if not transaction:
        print("No transactions yet.")
    else:
        print("\n========== TRANSACTION HISTORY ==========")
        for index, record in enumerate(transaction, 1):
            print(f"\nTransaction {index}:")
            print(record)
        print("=========================================\n")
