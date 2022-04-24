from credentials import Credentials
from user import user



def main():
    print("Hello Welcome to your password locker site. What is your name?")
    name = input()

    print(f"Hello {name}. what would you like to do?")
    print('\n')


while True:
        print("Hello. Welcome back to Password Locker!")
        print('\n')
        print('Create a login username and a password')
        print('\n')
        print('Enter username')
        username =  input()
        print('Enter password')
        user_password = input()

        print('To login in, Enter your username')
        input_username = input()
        if (input_username == username):
            print('Enter your password')
            input_password = input()
            if (input_password == user_password):
                print("Use these short codes : cr - create a new account, di - display accounts, fi -find an account, ex -exit the account list ")

                short_code:any = input().lower()

                if short_code == "ca":
                    print("New Account")
                    print("-"*10)

                    print ("Account name ...")
                    acc_name = input()

                    print("Username ...")
                    user_name = input()

                    print("Password ...")
                    user_password = input()

                    save_credential(create_account(acc_name, user_name, user_password)) # create and save new account.
                    print('\n')
                    print(f"New {acc_name} Account Created")
                    print('\n')
                    if short_code == "da":

                if display_accounts:
                        print("Here is a list of all your accounts")
                        print('\n')

                        for account in display_accounts():
                            print(f"{account.acc_name} {account.user_name} .....{account.password}")

                        print('\n')

                        print('Enter the name of an account you wish to delete.')
                        del_name= input()    