class Credentials:
    """
    Class that generates new instances of credentials.
    """

    accounts_list = [] 
    

    def __init__(self, acc_name, user_name, user_password):
        '''
        method that defines variables to be used
        '''

        self.acc_name = acc_name
        self.user_name = user_name
        self.user_password = user_password

    # @classmethod
    def display_accounts(self):
        '''
        method that returns the accounts_list
        '''
        return self.accounts_list
    
        
    @classmethod
    def save_credential(cls):

        '''
        save_credential method saves account objects into accounts_list
        '''

        Credentials.accounts_list.append(cls)
    
    @classmethod
    def delete_account(cls):
        '''
        method that deletes a saved account from the account list
        '''
        Credentials.accounts_list.remove(cls)    