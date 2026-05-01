from database import create_tables
from customer_manager import add_customer, view_customers
from currency_manager import add_currency, view_currencies
from account_manager import create_account, view_accounts
from exchange_manager import create_exchange, view_exchanges

def menu():
    print("\n==== Finance System ====")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Add Currency")
    print("4. View Currencies")
    print("5. Create Account")
    print("6. View Accounts")
    print("7. Create Exchange")
    print("8. View Exchanges")
    print("9. Exit")

def main():
    create_tables()

    while True:
        menu()
        choice = input("Select an option (1-9): ")

        if choice == '1':
            fn = input("First name: ")
            ln = input("Last name: ")
            email = input("Email: ")
            add_customer(fn, ln, email)

        elif choice == '2':
            for c in view_customers():
                print(c)

        elif choice == '3':
            code = input("Currency code (USD, NZD): ")
            name = input("Currency name: ")
            rate = float(input("Rate to USD: "))
            add_currency(code, name, rate)

        elif choice == '4':
            for c in view_currencies():
                print(c)

        elif choice == '5':
            acc_type = input("Account type: ")
            currency = input("Currency code: ")
            create_account(acc_type, currency)

        elif choice == '6':
            for a in view_accounts():
                print(a)

        elif choice == '7':
            from_c = input("From currency: ")
            to_c = input("To currency: ")
            rate = float(input("Exchange rate: "))
            fee = float(input("Fee: "))
            create_exchange(from_c, to_c, rate, fee)

        elif choice == '8':
            for e in view_exchanges():
                print(e)

        elif choice == '9':
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()