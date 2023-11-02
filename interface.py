def create_bank_interface(balance):
    # balance = 100
    def bank_interface(action, amount=0):
        def deposit(amount):
            nonlocal balance
            balance += amount
            return balance

        def withdraw(amount):
            nonlocal balance
            if balance - amount < 0:
                print('ERROR')
            else:
                balance -= amount
            return balance

        def print_balance():
            nonlocal balance
            print(balance)

        def exit_interface():
            print('you are exiting the interface')
            exit()

        if action == 1:
            return deposit(amount)
        elif action == 2:
            return withdraw(amount)
        elif action == 3:
            print_balance()
        elif action == 4:
            exit_interface()
        else:
            print('Invalid action')
    return bank_interface


bank_interface_instance = create_bank_interface(100)
bank_interface_instance(1, 50)  # Deposit
bank_interface_instance(2, 30)  # Withdraw
bank_interface_instance(3)  # Print balance
# you should see 120
bank_interface_instance(4)  # Exit
