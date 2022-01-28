import unittest #imported unitest module
from accounts import Account

class TestAccount(unittest.TestCase):
    '''
    unittest.TestCase: a class that helps in creating test accounts
    ''' 

    def tearDown(self):
        '''
        Specifies may array
        '''
        Account.usr_accounts = []

    def setUp(self):
        ''' 
        this test runs before all other tests run
        '''
        self.new_accounts = Account('Blueman', '133131')

    def test_init(self):
        '''
        this checks if the objects is initialized properly
        '''
        self.assertEqual(self.new_accounts.usr_name, 'Blueman')
        self.assertEqual(self.new_accounts.password, '133131')

    def test_save_account(self):
        '''
        this checks if the objects is saved properly
        '''
        self.new_account.save_account() #saving the new account
        test_account = Account('test0', 'test1', 'test2', 'test3', 'test4', 'test5')
        test_account.save_account()
        self.assertEqual(len(Account.user_accounts), 1)

    def test_save_multiple_accounts(self):
        '''
        this checks if the account has been saved
        '''
        self.new_account.save_account() 
        test_account = Account('test0', 'test1', 'test2', 'test3', 'test4', 'test5')
        test_account.save_account()
        self.assertEqual(len(Account.usr_accounts), 2)

    def test_find_account_by_user_name(self):
        '''
        this checks if the function to get usr_accounts works
        '''
        self.new_account.save_account()
        test_account = Account('test0', 'test1', 'test2', 'test3', 'test4', 'test5')
        test_account.save_account()
        found_account = Account.find_by_usr_name('test4')
        self.assertEqual(found_account.usr_name, test_account.usr_name) 

    def test_del_account(self):
        '''
        this checks if account can be deleted
        '''
        self.new_account.save_account()
        test_account = Account('test0', 'test1', 'test2', 'test3', 'test4', 'test5')
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Account.usr_accounts), 1) 

    def test_account_exists(self):
        '''
        this checks if account exists and returns true/false
        '''
        self.new_account.save_account()
        test_account = Account('test0', 'test1', 'test2', 'test3', 'test4', 'test5')
        test_account.save_account()
        account_exists = Account.account_exists('test2')
        self.assertTrue(account_exists)

    def test_display_account(self):
        '''
        this checks if the display function works properly
        '''
        self.assertEqual(Account.display_accounts(),                    Account.usr_accounts) 

if __name__ == '__main__':
    unittest.main()