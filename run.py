from credentials import Credentials
from user import User


def create_account(acc_name, user_name, user_password):
    new_account= Credentials(acc_name, user_name, user_password)
    return new_account


def save_credential (credentials):
    '''
    Function to delete a credentials
    '''
    credentials.save_credential()

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()


def del_account(Credentials):
    '''
    Function to delete an account
    '''
    Credentials.delete_account()

def main():
    print("Hello Welcome to your password locker site. What is your name?")
    name = input()
    print('\n')
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
            
                short_code= input().lower()

                if short_code == "cr":
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
                elif short_code == "di":
                    if display_accounts:
                        print("Below is a list of all your accounts")
                        print('\n')

                        for account in display_accounts():
                            print(f"{account.acc_name}{account.user_name} .....{account.user_password}")

                        print('\n')

                    else:
                        print(' account not found,kindly create a new account')

                else:
                        print('\n')
                        print("No accounts saved yet")
                        print('\n')
            else:
                print('Wrong Password')

        else:
            print('Wrong Username')


if __name__ == '__main__':

    main()   