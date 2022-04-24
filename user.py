class User:
    """
    Class that generates a new instance of a user password.
    """
    user_list=[]
    acc_name=''
    user_name= ''
    user_password=''

    def __init__(self, acc_name,user_name, user_password):
        '''
        method that defines variables to be used
        '''
    
        self.user_name = user_name
        self.user_password= user_password
        self.acc_name=acc_name

    @classmethod
    def save_password(cls):

        '''
        a method that saves password.
        '''

        User.user_password

