import random


# Bank information
class Bank:
    def __init__(self, name, ifsc, branch, address):
        self.name = name  # Public
        self.ifsc = ifsc  # Public
        self.branch = branch  # Public
        self.address = address  # Public


# User class with attributes
class User:
    def __init__(self, name, address, phone, account_no, balance):
        self.name = name  # Public
        self.address = address  # Public
        self.phone = phone  # Public
        self.__account_no = account_no  # Private
        self.__balance = balance  # Private

    def generate_otp(self):
        return random.randrange(1000, 10000)  # Public

    def withdraw(self, amount):
        if self.__balance >= amount:  # Protected
            self.__balance -= amount
            return True
        else:
            return False

    def credit(self, amount):
        self.__balance += amount  # Protected

    def get_balance(self):
        return self.__balance  # Public

    def get_account_no(self):
        return self.__account_no  # Public


# Function to handle login and OTP generation
def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    if email in users_database and password == "password":
        user = users_database[email]
        otp = user.generate_otp()
        print(f"OTP sent to your registered phone number: {otp}")
        return user, otp
    else:
        print("Invalid OTP")
        return None, None


# Main program
def main():
    bank = Bank("Example Bank", "EXMP1234", "Main Branch", "123 Street Rd, City")
    user, otp = login()

    if user is not None:
        entered_otp = int(input("Enter the OTP sent to your phone: "))
        if entered_otp == otp:
            print(f"Welcome, {user.name}!\n")
            print(f"Account Information:")
            print(f"Name: {user.name}")
            print(f"Address: {user.address}")
            print(f"Phone: {user.phone}")
            print(f"Account No: {user.get_account_no()}")  # Accessing account number through public method.
            print(f"Balance: {user.get_balance()}")  # Accessing balance through public method.

            amount = float(input("Enter the amount to withdraw: "))
            if user.withdraw(amount):
                print(f"Withdrawal successful. New balance: {user.get_balance()}")
            else:
                print("Insufficient funds.")

            amount = float(input("Enter the amount to credit: "))
            user.credit(amount)
            print(f"Credit successful. New balance: {user.get_balance()}")


# Database of users (simulated for this example)
users_database = {
    "user1@example.com": User("John Doe", "123 Main St", "1234567890", "123456789", 1000),
    "user2@example.com": User("Jane Smith", "456 Oak Ave", "0987654321", "987654321", 1500)
}

if __name__ == "__main__":
    main()