class Password:
    usr_password = []
    def __init__(self, ppage, password):
        self.page = ppage
        self.password = password

    def save_ppage(self):
        '''
        This saves the password
        '''
        Password.usr_password.remove(self)
        
    def delete_ppage(self):
        '''
        This deletes a saved password
        '''
        Password.usr_password.remove(self)

    @classmethod
    def display_password(cls):
        '''
        this displays passwords
        '''
        return cls.usr_password

    @classmethod
    def find_by_ppage(cls, pager):
        '''
        this checks if the password already exist 
        '''
        for pagy in cls.usr_password:
            if pagy.ppage == pager:
                return pagy

    @classmethod
    def password_exists(cls, pager):
        for pagy in cls.usr_password:
            if pagy.ppage == pager:
                return pagy
        return False