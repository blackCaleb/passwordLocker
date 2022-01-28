class Accounts:
    usr_accounts = [] #Empty user account lists
    def __init__(self, usr_name, password):
        self.usr_name = usr_name
        self.password = password

    def save_accounts(self):
        '''
        this method saves accounts into usr_accounts
        '''
        Accounts.usr_accounts.append(self)

    def delete_accounts(self):
        '''
        this deletes a specific account from usr_accounts
        '''
        Accounts.usr_accounts.remove(self)

    @classmethod
    def find_by_usr_name(cls, usr_name):
        '''
        this checks if the user name already exist in usr_accounts and if it does it returns account
        '''
        for account in cls.usr_accounts:
            if account.usr_name == usr_name:
                return account

    @classmethod
    def account_exists(cls, usr_name):
        '''
        this seaches the usr name entered by the user in present array and returns true/false
        '''
        for account in cls.usr_accounts:
            if account.usr_name == usr_name:
                return True
            return False

    @classmethod
    def display_accounts(cls):
        '''
        this displays accounts
        '''
        return cls.usr_accounts