import petroleum_function 

transaction = []

while True:
    menu = """
    WELCOME TO GBeda Station!

    Available petroleum
    1 -> Buy petroleum
    2 -> Show Transactions
    3 -> Exit
    """
    print(menu)

    user = input("Enter operation: ")

    match user: 
        case "1":
            print("""
            Available petroleum:
            1-> Petrol = 650/Liter
            2-> Diesel = 720/Liter
            3-> Kerosene = 550/Liter
            4-> Gas = 480/Liter
            """)
            
            petrol = input("Enter operation: ")
            match petrol:
                case "1":
                    petroleum_function.buy_petrol("", transaction)
                case "2":
                    petroleum_function.get_diesel("", transaction)
                case "3":
                    petroleum_function.get_kerosene("", transaction)
                case "4":
                    petroleum_function.get_gas("", transaction)

        case "2":
            print("\nTransaction History:")
            petroleum_function.get_transaction_history(transaction)

        case "3":
            print("Exiting...")
            break
