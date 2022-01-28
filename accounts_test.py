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
        Accounts.usr_accounts = []

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
        