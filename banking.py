# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
    if balance == 0:
        print("Your Broke Fool!")
    else:
        print("I guess you got some coins, still ugly though!")


def deposit():
    amount = float(input("Enter an amount to despoit: "))

    if amount < 0:
        print("Enter Some Money, and stop Wasting my time ")
        return 0
    else:
        print("😂😂😂 Look who finally got some money")
        return amount


def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("I don't know why you tryna take money, your broke and got no motion 🤦🏾‍♂️")
    elif amount < 0:
        print("Yeah your dumb, enter a number!")
    else:
        print("Damn your taking money already, knew you couldn't stay rich 👎🏾")
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdrawl")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Non Valid Choice")

    print("Thank you, Have a nice day!")


if __name__ == '__main__':
    main()
