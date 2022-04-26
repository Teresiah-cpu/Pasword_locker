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
def find_credential(acc_name):
    """
    find a credential from the credential list using account
    """
    return Credentials.find_credential(acc_name)

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
    while True:
        print("Hello. Welcome  to Password Locker!")
        print('\n')
        print('Create account')
        print('\n')
        print('Enter firstname')
        username =  input()
        print('Enter lastname')
        username =  input()
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

            
            
                short_code= input("").lower().strip()

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
                    # print(f"New {acc_name} Account Created")

                
                    # print("di - display accounts, fi -find an account, ex -exit the account list ")

                    # print('\n')
                elif short_code == "di":
                    if display_accounts:
                        print("Here are your account details")
                        print(f"ACCOUNT_NAME: {acc_name}\nUSERNAME: {user_name}\nUSER_PASSWORD: {user_password}")
                        # print("Below is a list of all your accounts")
                        # print('\n')

                        # for account in display_accounts():
                        #     print(f"{account.acc_name}{account.user_name} .....{account.user_password}")

                        # print('\n')

                    else:
                        print(' account not found,kindly create a new account')
                elif short_code == "fi": 
                    print("Enter the Account Name you want to search for")
                    search_name = input().lower()
                    if find_credential(search_name):
                        search_credential = find_credential(search_name)
                        print(f"Account Name : {search_credential.acc_name}")
                        print('-' * 60)
                        print(f"User Name: {search_credential.user_name} Password :{search_credential.user_password}")
                        print('-' * 60)
                    else:
                        print("The Credential does not exist")
                        print('\n')
                else:
                    print('choose short code to continue')        
                    
            else:
                print('Wrong Password')

        else:
            print('Wrong password')
    else:
        print('Wrong username')


if __name__ == '__main__':

    main()   