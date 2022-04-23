class user:
    """
    Class that allows user to create a user password.
    """
    user_name= ''
    user_password=''

    def __init__(self, user_name, user_password):
        '''
        method that defines variables to be used
        '''

        self.user_name = user_name
        self.user_password= user_password